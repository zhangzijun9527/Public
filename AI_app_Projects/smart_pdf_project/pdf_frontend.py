import gradio as gr
import requests

# 🚨 注意：请求 Docker 内部的后端服务名 backend
BACKEND_URL = "http://backend:8010"


def upload_and_process(file):
    if file is None:
        return '❌ 请先上传 PDF 文件'
    try:
        with open(file.name, 'rb') as f:
            files = {'file': (file.name, f, 'application/pdf')}
            # 🚨 请求新的流式上传接口
            response = requests.post(f'{BACKEND_URL}/api/pdf/upload_and_rebuild', files=files, timeout=120)

        data = response.json()
        if data.get('status') == 'success':
            return f"✅ {data.get('message')}"
        else:
            return f"❌ 解析失败: {data.get('message')}"
    except Exception as e:
        return f"❌ 发生错误: {str(e)}"


def chat_with_pdf(question, history):
    if not question.strip(): return ""
    try:
        response = requests.post(f"{BACKEND_URL}/api/pdf/ask", json={"question": question}, timeout=60)
        data = response.json()

        if data.get("status") == "error":
            return data.get("reply", "系统出错了")
        return data.get("reply", "未查到信息")
    except Exception as e:
        return f"❌ 连接后端失败: {str(e)}"


with gr.Blocks(title="智能 PDF 论文助手") as demo:
    gr.Markdown("# 📚 智能 PDF 论文阅读助手 (RAG)")
    gr.Markdown("上传你的英文 PDF 论文，让 AI 帮你用中文划重点！")

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="上传 PDF 文件", file_types=[".pdf"])
            upload_btn = gr.Button("🚀 解析并入库", variant="primary")
            status_output = gr.Textbox(label="系统状态", interactive=False)
            upload_btn.click(fn=upload_and_process, inputs=file_input, outputs=status_output)

        with gr.Column(scale=2):
            chatbot = gr.ChatInterface(
                fn=chat_with_pdf,
                title="与论文对话"
            )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)




