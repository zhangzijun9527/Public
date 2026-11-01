import os
import re
import requests
import pymupdf as fitz
import chromadb
from pathlib import Path
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from dotenv import load_dotenv

# ================= 1. 环境变量与配置 =================
load_dotenv()  # 从 .env 文件加载环境变量

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
BAILIAN_API_KEY = os.getenv("BAILIAN_API_KEY")

if not DEEPSEEK_API_KEY or not BAILIAN_API_KEY:
    raise ValueError(" 缺少 API Key，请检查 .env 文件中的 DEEPSEEK_API_KEY 和 BAILIAN_API_KEY")

# 阿里云百炼 Embedding 接口配置
EMBEDDING_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings"
EMBEDDING_MODEL_NAME = "text-embedding-v3"


def get_embeddings(texts):
    """
    【核心逻辑】：调用阿里云百炼 API 获取文本向量。
    【踩坑点】：阿里云限制单次请求的文本数量，必须分批发送，否则会报错。
    """
    headers = {
        "Authorization": f"Bearer {BAILIAN_API_KEY}",
        "Content-Type": "application/json"
    }

    all_embeddings = []
    batch_size = 10  # 每次发 10 条文本，防止超出 API 限制

    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        payload = {
            "model": EMBEDDING_MODEL_NAME,
            "input": batch_texts
        }
        try:
            response = requests.post(EMBEDDING_URL, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            for item in data["data"]:
                all_embeddings.append(item["embedding"])
        except Exception as e:
            print(f"调用 Embedding API 失败: {e}")
            raise e

    return all_embeddings


# ================= 2. 向量数据库初始化 =================
print(" 正在初始化向量数据库...")
current_dir = Path(__file__).parent
db_path = current_dir / 'chroma_db'
# 使用 PersistentClient 将数据持久化到本地硬盘
chroma_client = chromadb.PersistentClient(path=str(db_path))
collection = chroma_client.get_or_create_collection(name="pdf_knowledge")

app = FastAPI(title='智能PDF论文理解助手')


# 定义前端传过来的 JSON 结构
class AskRequest(BaseModel):
    question: str


# ================= 3. 核心接口 1：上传与解析 =================
@app.post("/api/pdf/upload_and_rebuild")
async def upload_and_rebuild(file: UploadFile = File(...)):
    try:
        # 1. 异步读取文件内容到内存中
        content = await file.read()
        doc = fitz.open(stream=content, filetype="pdf")
        # 2. 提取所有页面的文本
        full_text = "".join([page.get_text("text") + "\n" for page in doc])
        doc.close()

        # 3. 正则清洗：将多个连续空格/换行替换为一个空格
        text = re.sub(r'\s+', ' ', full_text)

        # 4. 滑动窗口切片（Chunk Size: 500, Overlap: 50）
        chunk_size = 500
        overlap = 50
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            # 过滤掉纯空白的切片
            if chunk_text.strip():
                chunks.append(chunk_text)
            start += chunk_size - overlap

        if not chunks:
            return {"status": "error", "message": "未能从 PDF 中提取到有效文本。"}

        # 5. 重建库之前，先删掉旧的向量数据
        existing_data = collection.get()
        if existing_data['ids']:
            collection.delete(ids=existing_data['ids'])

        # 6. 调用阿里云 API 生成向量
        embeddings = get_embeddings(chunks)

        # 7. 自定义 ID，存入 ChromaDB
        ids = [f"pdf_chunk_{i}" for i in range(len(chunks))]
        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids
        )

        return {"status": "success", "message": f" 成功入库！当前库中共有 {collection.count()} 条数据！"}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": f"解析失败: {str(e)}"}


# ================= 4. 核心接口 2：智能问答 =================
@app.post('/api/pdf/ask')
def ask_pdf(request: AskRequest):
    try:
        # 1. 把用户的问题变成向量
        query_embeddings = get_embeddings([request.question])

        # 2. 去向量库里找最相似的 4 个片段
        results = collection.query(
            query_embeddings=query_embeddings,
            n_results=4
        )

        # 3. 异常兜底处理（防止空数据报错）
        if not results['documents'] or not results['documents'][0]:
            return {"status": "error", "reply": "库里没数据，请先上传 PDF！"}

        valid_docs = [doc for doc in results['documents'][0] if doc is not None]
        if not valid_docs:
            return {"status": "success", "reply": "这篇论文中没有找到相关内容。"}

        # 4. 把检索到的几段话拼起来，作为背景资料
        context = '\n'.join(valid_docs)

        # 5. 构造请求，发给 DeepSeek
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": f"你是一个专业的学术助手。请根据以下资料回答：\n\n{context}"},
                {"role": "user", "content": request.question}
            ]
        }

        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        # 6. 提取大模型的回答并返回给前端
        answer = response.json()['choices'][0]['message']['content']
        return {'status': 'success', 'reply': answer}

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn AI_app_Projects.smart_pdf_project.pdf_api:app --port 8010
