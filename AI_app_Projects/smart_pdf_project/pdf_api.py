import os
import re
import requests
import pymupdf as fitz
import chromadb
from pathlib import Path
from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from dotenv import load_dotenv

# ================= 1. 环境变量配置 =================
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
BAILIAN_API_KEY = os.getenv("BAILIAN_API_KEY")  # 你的阿里云百炼 Key

if not DEEPSEEK_API_KEY or not BAILIAN_API_KEY:
    raise ValueError("❌ 缺少 API Key，请检查 .env 文件中的 DEEPSEEK_API_KEY 和 BAILIAN_API_KEY")

# 阿里云百炼 Embedding 配置
EMBEDDING_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings"
EMBEDDING_MODEL_NAME = "text-embedding-v3"


def get_embeddings(texts):
    """调用阿里云百炼 API 获取向量（自带分批，防止超出限制）"""
    headers = {
        "Authorization": f"Bearer {BAILIAN_API_KEY}",
        "Content-Type": "application/json"
    }

    all_embeddings = []
    batch_size = 10  # 阿里云限制单次输入不能太多

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
            print(f"❌ 调用 Embedding API 失败: {e}")
            raise e

    return all_embeddings


# ================= 2. 向量库初始化 =================
print("⏳ 正在初始化向量数据库...")
current_dir = Path(__file__).parent
db_path = current_dir / 'chroma_db'
chroma_client = chromadb.PersistentClient(path=str(db_path))
collection = chroma_client.get_or_create_collection(name="pdf_knowledge")

app = FastAPI(title='智能PDF论文理解助手')


class AskRequest(BaseModel):
    question: str


# ================= 3. 核心接口 1：上传解析 =================
@app.post("/api/pdf/upload_and_rebuild")
async def upload_and_rebuild(file: UploadFile = File(...)):
    try:
        content = await file.read()
        doc = fitz.open(stream=content, filetype="pdf")
        full_text = "".join([page.get_text("text") + "\n" for page in doc])
        doc.close()

        # 清理多余空白字符
        text = re.sub(r'\s+', ' ', full_text)

        # 文本切片
        chunk_size = 500
        overlap = 50
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            if chunk_text.strip():  # 过滤空数据
                chunks.append(chunk_text)
            start += chunk_size - overlap

        if not chunks:
            return {"status": "error", "message": "未能从 PDF 中提取到有效文本。"}

        # 删除旧数据
        existing_data = collection.get()
        if existing_data['ids']:
            collection.delete(ids=existing_data['ids'])

        # 获取向量并入库
        embeddings = get_embeddings(chunks)
        ids = [f"pdf_chunk_{i}" for i in range(len(chunks))]

        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=ids
        )

        return {"status": "success", "message": f"🎉 成功入库！当前库中共有 {collection.count()} 条数据！"}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": f"解析失败: {str(e)}"}


# ================= 4. 核心接口 2：智能问答 =================
@app.post('/api/pdf/ask')
def ask_pdf(request: AskRequest):
    try:
        # 1. 问题向量化
        query_embeddings = get_embeddings([request.question])

        # 2. 检索最相关的 4 个片段
        results = collection.query(
            query_embeddings=query_embeddings,
            n_results=4
        )

        # 3. 防弹处理：过滤掉空数据
        if not results['documents'] or not results['documents'][0]:
            return {"status": "error", "reply": "库里没数据，请先上传 PDF！"}

        valid_docs = [doc for doc in results['documents'][0] if doc is not None]
        if not valid_docs:
            return {"status": "success", "reply": "这篇论文中没有找到相关内容。"}

        # 4. 拼接上下文
        context = '\n'.join(valid_docs)

        # 5. 调用 DeepSeek 生成回答
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

        answer = response.json()['choices'][0]['message']['content']
        return {'status': 'success', 'reply': answer}

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn AI_app_Projects.smart_pdf_project.pdf_api:app --port 8010
