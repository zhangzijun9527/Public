import os
# 1. 【极其重要】必须在所有 AI 库导入之前，强制指定镜像和清空代理
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''
os.environ['NO_PROXY'] = 'api.deepseek.com,localhost,127.0.0.1,hf-mirror.com'

import re
import chromadb
import pymupdf as fitz
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv

# 2. 初始化环境
load_dotenv()
deepseek_key = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=deepseek_key, base_url="https://api.deepseek.com/v1")

#  加载向量模型
model = SentenceTransformer("BAAI/bge-small-zh-v1.5")

# 2.连接向量库
chroma_client = chromadb.PersistentClient(path="../chroma_db")
collection = chroma_client.get_or_create_collection(name='pdf_knowledge')
def process_pdf_to_db():
    doc = fitz.open('test.pdf')
    full_text = ""
    for page in doc:
        full_text += page.get_text('text')+'\n'
    doc.close()
    #清洗与切片
    text = re.sub(r'\s+', '', full_text)
    sentences = re.split(r'(?<=[.!?])\s+',text)

    chunks = []
    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk) +len(sentence) < 500:
            current_chunk += sentence + ''
        else:
            if current_chunk.strip(): chunks.append(current_chunk.strip())
            current_chunk = sentence + ''
    if current_chunk.strip(): chunks.append(current_chunk.strip())

    # 3.批量向量化并存入chromaDB
    print(f'正在将{len(chunks)}个片段存入向量数据库')

    #  为了不撑爆内存，分批次存入
    batch_size = 50
    for i in range(0,len(chunks),batch_size):
        batch_chunks = chunks[i:i+batch_size]
        embeddings = model.encode(batch_chunks).tolist()

        #构造唯一ID
        ids = [f'pdf_chunk_{i+j}'for j in range(len(batch_chunks))]
        collection.add(
            documents=batch_chunks,
            embeddings=embeddings,
            ids=ids
        )
    print('数据载入完毕')

def ask_pdf(question):
    print(f'用户提问：{question}')

    #  1.去向量检索最相似的两个片段
    query_embedding = model.encode([question]).tolist()
    results = collection.query(query_embeddings=query_embedding,n_results=2)
    context = '\n'.join(results['documents'][0])

    #  2.构造prompt
    prompt = f"""你是一个专业的学术助手，请根据以下参考资料回答用户的问题。如果资料中找不到答案，请直接回复不知道。
    【参考资料】：
    {context}
    """

    #  3.发给大模型
    response = client.chat.completions.create(
        model = 'deepseek-chat',
        messages = [
            {'role':'system','content':prompt},
            {'role':'user','content':question}
        ]
    )

    print(response.choices[0].message.content)

if __name__ == '__main__':
    process_pdf_to_db()

