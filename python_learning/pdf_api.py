import os
from pathlib import Path

os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''
os.environ['NO_PROXY'] = 'api.deepseek.com,localhost,127.0.0.1,hf-mirror.com'

import re
import pymupdf as fitz
import chromadb
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv

#  初始化环境
current_dir = Path(__file__).parent
load_dotenv(dotenv_path=current_dir / '.env')
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=deepseek_key, base_url="https://api.deepseek.com/v1", max_retries=3, timeout=30.0)

print(" 正在加载向量模型...")
embed_model = SentenceTransformer('BAAI/bge-small-zh-v1.5')

db_path = current_dir / 'chroma_db'
chroma_client = chromadb.PersistentClient(path=str(db_path))
collection = chroma_client.get_or_create_collection(name="pdf_knowledge")

print(f"服务初始化完毕！当前向量库数据量: {collection.count()} 条")
app = FastAPI(title='智能PDF论文理解助手')


class AskRequest(BaseModel):
    question: str


# ================= 接口一：一键解析并入库 =================
@app.get("/api/pdf/rebuild_db")
def rebuild_db():
    pdf_path = current_dir / "test.pdf"
    if not pdf_path.exists():
        return {"status": "error", "message": "找不到 test.pdf，请确保它和代码在同一个文件夹！"}

    print(f"开始读取并解析: {pdf_path}")
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text("text") + "\n"
        doc.close()

        # 1. 先把换行符和多余空格清理掉
        text = re.sub(r'\s+', ' ', full_text)

        #  清空旧数据
        existing_data = collection.get()
        if existing_data['ids']:
            collection.delete(ids=existing_data['ids'])
            print('清理完毕')

        # 2.  关键：加上这行，把那些恶心的 "Just Accepted" 废话全删掉！
        # 注意：这里用 replace 简单粗暴地删掉常见的废话词组，比正则更不容易出错
        text = text.replace("“Just Accepted” manuscripts have been peer-reviewed and accepted for publication.", "")
        text = text.replace(
            "“Just Accepted” manuscripts have been fully peer reviewed, but should not be considered the official version of record.",
            "")

        # 3. 开始固定字数切片
        chunk_size = 500
        overlap = 50
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunks.append(text[start:end])
            start += chunk_size - overlap

        # 4. 向量化并入库
        print(f"正在向量化并存入 {len(chunks)} 个片段...")
        embeddings = embed_model.encode(chunks).tolist()
        ids = [f"pdf_chunk_{i}" for i in range(len(chunks))]

        collection.add(documents=chunks, embeddings=embeddings, ids=ids)

        return {"status": "success", "message": f"🎉 成功入库！当前库中共有 {collection.count()} 条数据！"}
    except Exception as e:
        return {"status": "error", "message": f"解析失败: {str(e)}"}


# ================= 接口二：智能问答 =================
@app.post('/api/pdf/ask')
def ask_pdf(request: AskRequest):
    try:
        query_embeddings = embed_model.encode([request.question]).tolist()
        results = collection.query(query_embeddings=query_embeddings, n_results=6)

        if not results['documents'] or len(results['documents'][0]) == 0:
            return {"status": "error", "reply": "库里没数据，请先调 rebuild_db！"}

        context = '\n'.join(results['documents'][0])

        prompt = f"你是一个专业的学术助手。请根据以下资料回答：\n\n{context}"

        response = client.chat.completions.create(
            model='deepseek-chat',
            messages=[{'role': 'system', 'content': prompt},
                      {'role': 'user', 'content': request.question}]
        )

        return {
            'status': 'success',
            'reply': response.choices[0].message.content,
            'source_docs': results['documents'][0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# uvicorn python_learning.pdf_api:app --port 8005 --reload
