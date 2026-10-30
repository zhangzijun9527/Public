import gradio as gr
import requests
import shutil
from pathlib import Path
import os

BACKEND_URL = 'http://127.0.0.1:8010'
current_dir = Path(__file__).parent

def upload_and_process(file):
    if file is None:
        return  '上传失败，请上传pdf文件'

    try:
        # 1.将用户上传的文件保存到本地，命名为 test.pdf
        #   后端rebuild_db 接口可以读取
        target_path =  current_dir / 'test.pdf'
        shutil.copy(file.name, target_path)

        # 2. 调用后端的问答接口，触发重新解析和向量化
        response = requests.get(f'{BACKEND_URL}/api/pdf/rebuild_db')
        data = response.json()

        if data.get('status') == 'success':
            return f'{data.get('message')}'
        else:
            return f'解析失败：{data.get("message")}'
    except Exception as e:
        return f'发生错误：{str(e)}'

def chat_with_pdf(question,histry):
    if not question.strip(): return ""
    try:
        # 调用后端的问答接口
        response = requests.post(f'{BACKEND_URL}/api/pdf/ask',json={'question':question},timeout=60)
        data = response.json()

        if data.get('status') == 'error':
            return data.get('reply','系统出错')

        reply = data.get('reply','未查到信息')

        # 把检索到的参考资料拼接到回答下面，实现溯源
        sources = data.get('source_docs',[])
        if sources:
            reply += '\n---------------\n答案参考以下片段'
            for i, src in enumerate(sources[:2]):  # 截取前两段
                # 截取前150个字符
                reply += f'片段{i+1}:{src[:150]}'
        return reply
    except Exception as e:
        return f'连接后端失败：{str(e)}'

#  =======搭建gradio界面=======
with gr.Blocks(title='智能PDF论文助手') as demo:
    gr.Markdown('# 智能PDF论文阅读助手(RAG)')
    gr.Markdown('上传你的英文 PDF 论文，让AI帮你用中文划重点！')

    with gr.Row():
        with gr.Column(scale=1):
            # 文件上传组件
            file_input = gr.File(label='上传PDF文件')
            upload_btn = gr.Button('解析入库',variant='primary')
            status_output = gr.Textbox(label='系统状态',interactive=False)

            # 绑定上传按钮事件
            upload_btn.click(fn=upload_and_process,inputs=file_input,outputs=status_output)

        with gr.Column(scale=2):
            # 聊天组件
            chatbot = gr.ChatInterface(
                fn=chat_with_pdf,
                title='与论文对话',
                examples=['这篇论文研究什么？','论文的主要结论是什么？','请用三句话总结这篇论文。']
            )

if __name__ == '__main__':
    demo.launch()




