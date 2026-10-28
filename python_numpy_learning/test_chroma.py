import os
os.environ['HF_ENDPOINT']='https://hf-mirror.com'

import chromadb
from sentence_transformers import SentenceTransformer

def main():
    model = SentenceTransformer('BAAI/bge-small-zh-v1.5')
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="car_knowledge")

    documents = [
        "2018款丰田卡罗拉，行驶里程4万公里，无重大事故，左前翼子板有轻微钣金修复痕迹。",
        "2016款本田思域，发生过一次追尾，更换过后保险杠，售价7万。",
        "宝马X1，2015年款，发动机有轻微漏油迹象，售价12万。"
    ]

    embeddings = model.encode(documents).tolist()
    collection.add(documents=documents, embeddings=embeddings, ids=["id1", "id2", "id3"])
    print("✅ 数据入库成功！")


if __name__ == "__main__":
    main()