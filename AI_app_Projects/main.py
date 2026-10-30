import os
from dotenv import load_dotenv
from pathlib import Path

# ==========================================
# 🌟 核心防坑一：必须在所有 AI 库导入之前，强制指定国内镜像源和防代理
# ==========================================
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''
os.environ['NO_PROXY'] = 'api.deepseek.com,localhost,127.0.0.1,hf-mirror.com'

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from openai import OpenAI
import chromadb
from sentence_transformers import SentenceTransformer

# ==========================================
# 🌟 核心防坑二：从 .env 文件安全加载密钥
# ==========================================
load_dotenv()

db_password = os.getenv("DB_PASSWORD")
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

if not db_password or not deepseek_key:
    raise ValueError("❌ 错误：没有找到环境变量，请检查 .env 文件是否配置正确！")

app = FastAPI(title="二手车 AI 智能中枢")

# ================= 1. 数据库配置 =================
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:{db_password}@localhost:3306/ai_learning"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ================= 2. 大模型配置 =================
client = OpenAI(
    api_key=deepseek_key,
    base_url="https://api.deepseek.com/v1",
    max_retries=3,
    timeout=30.0
)

# ================= 3. 向量数据库与模型配置 =================
print("1. 正在加载中文向量模型...")
embed_model = SentenceTransformer('BAAI/bge-small-zh-v1.5')

print("2. 正在连接本地 ChromaDB 向量数据库...")
# 获取绝对路径，确保不管在哪里启动都能找到
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "chroma_db")
chroma_client = chromadb.PersistentClient(path=db_path)
collection = chroma_client.get_or_create_collection(name="car_knowledge")
print("✅ 环境初始化完毕！")


# ================= 数据模型 =================
class AskRequest(BaseModel):
    question: str


# ================= 接口路由 =================

# 天王 1：传统查库（用于前端首页展示最新列表，不消耗 AI Token，极快）
@app.get("/api/cars")
def get_cars(limit: int = 5):
    try:
        with engine.connect() as conn:
            sql = text(
                f"SELECT id, car_name, fuel_type, CAST(new_price AS FLOAT) AS new_price FROM used_cars LIMIT {limit}")
            result = conn.execute(sql)
            cars = [dict(row._mapping) for row in result]
            return {"status": "success", "data": cars}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"数据库查询失败: {str(e)}")


# 天王 2：纯大模型问答（兜底方案，不查资料，直接靠大模型自身世界知识）
@app.post("/api/ask")
def ask_expert(request: AskRequest):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一个资深的二手车评估专家。"},
                {"role": "user", "content": request.question}
            ]
        )
        return {"status": "success", "reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))


# 天王 3：RAG 文本检索（查 ChromaDB，用于查事故记录、维修日志等长文本）
@app.post("/api/rag_ask")
def rag_ask(request: AskRequest):
    try:
        # 1. 向量化检索
        query_embedding = embed_model.encode([request.question]).tolist()
        results = collection.query(query_embeddings=query_embedding, n_results=2)
        context = "\n".join(results['documents'][0])

        # 2. 构造 Prompt
        prompt = f"仅根据以下参考资料回答问题，找不到就说不知道：\n{context}"

        # 3. 调用大模型
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": request.question}]
        )
        return {
            "status": "success",
            "reply": response.choices[0].message.content,
            "source_docs": results['documents'][0]
        }
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))


# 天王 4：Text-to-SQL（智能查 MySQL，用于复杂条件筛选）
@app.post("/api/smart_search")
def smart_search(request: AskRequest):
    try:
        # 1. 让大模型翻译 SQL
        prompt = f"""
        你是一个 MySQL 专家。当前数据库中有两张表：
        表1：used_cars (二手车表)
        列名：id, car_name, fuel_type, transmission, mileage, engine, power, seats, new_price。
        表2：quotes (名言表)
        列名：id, text, author。
        请根据用户的提问，判断应该查询哪张表，并写出一条标准的 MySQL 查询语句。
        要求：
        1. 只返回 SQL，不要解释，不要加 ```sql。
        2. 模糊搜索用 LIKE。最多返回5条。
        提问：{request.question}
        """
        res1 = client.chat.completions.create(model="deepseek-chat", messages=[{"role": "user", "content": prompt}])

        # 清理大模型可能带出来的 markdown 格式杂质
        generated_sql = res1.choices[0].message.content.strip().replace("```sql", "").replace("```", "").strip()

        # 2. 执行 SQL 查库
        with engine.connect() as conn:
            result = conn.execute(text(generated_sql))
            cars = [dict(row._mapping) for row in result]

        if not cars:
            return {"status": "success", "reply": "数据库中没有符合条件的数据。", "sql": generated_sql}

        # 3. 把查出来的数据发给大模型总结
        summary_prompt = f"用户提问：{request.question}\n数据库查出数据：{str(cars)}\n请用专业评估师语气回答用户。"
        res2 = client.chat.completions.create(model="deepseek-chat",
                                              messages=[{"role": "user", "content": summary_prompt}])

        return {"status": "success", "reply": res2.choices[0].message.content, "sql_query": generated_sql}
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"智能查库失败: {str(e)}")




# uvicorn AI_app_Projects.main:app --reload
# uvicorn AI_app_Projects.main:app --port 8001










