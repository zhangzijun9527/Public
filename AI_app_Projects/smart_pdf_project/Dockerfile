FROM python:3.10-slim

WORKDIR /app


# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


# 复制所有代码到容器
COPY . .

EXPOSE 8010
EXPOSE 7860

# 默认启动后端，前端在 compose 里会被 command 覆盖
CMD ["uvicorn", "pdf_api:app", "--host", "0.0.0.0", "--port", "8010"]