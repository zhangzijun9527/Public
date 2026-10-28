import gradio as gr
import requests

# 前端呼叫后端的专线
BACKEND_URL = "http://127.0.0.1:8001"

def chat_with_rag(user_message, history):
    if not user_message.strip(): return ""
    try:
        # 注意：这里呼叫的是 RAG 接口
        payload = {"question": user_message}
        response = requests.post(f"{BACKEND_URL}/api/rag_ask", json=payload, timeout=60)
        data = response.json()
        ai_reply = data.get("reply", "未查到相关信息")

        sources = data.get("source_docs", [])
        if sources:
            ai_reply += "\n\n---\n**📚 参考了以下资料：**\n"
            for src in sources: ai_reply += f"- *{src}*\n"
        return ai_reply
    except Exception as e:
        return f"❌ 连接后端失败：{str(e)}"

demo = gr.ChatInterface(
    fn=chat_with_rag,
    title="🚗 二手车 AI 评估专家",
    description="基于 RAG 向量检索与大模型技术。你可以问我：'哪辆车出过事故？'",
    examples=["哪辆车被撞过？", "卡罗拉有事故吗？", "有没有漏油的车？"]
)

if __name__ == "__main__":
    demo.launch()










