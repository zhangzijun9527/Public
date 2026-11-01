# 🚀 My AI Application Development Portfolio

这里记录了我（大二）在学习并实战的 AI 应用开发项目。核心聚焦于 **RAG（检索增强生成）**、**LLM 应用落地** 与 **云端工程化部署**。基于 `Python + FastAPI + LLM API + ChromaDB + Docker` 构建。

## 📁 项目目录

### 1. 📚 智能 PDF 论文阅读助手 (SmartPDF RAG)
- **简介**：基于 RAG 架构的长文本解析工具。支持上传 PDF、正则清洗、滑动窗口切块、向量化检索与大模型精准总结。**已通过 Docker 部署至云服务器。**
- **核心亮点**：针对云服务器资源受限场景，将本地 Embedding 模型无缝重构为**阿里云百炼 API**，实现冷启动秒级响应，并解决了向量维度的平滑迁移。
- **核心技术**：`PyMuPDF` | `ChromaDB` | `阿里云百炼 (text-embedding-v3)` | `DeepSeek API` | `FastAPI` | `Gradio` | `Docker`
- **详情请点击文件夹查看。**

### 2. 🚗 二手车数据大模型平台 (Used Car AI)
- **简介**：融合数据清洗、数据库存储与 Text-to-SQL 的智能数据问答系统。
- **核心技术**：`Pandas` | `MySQL` | `FastAPI` | `DeepSeek API`。

## 🛠️ 全局技术栈 (Tech Stack)

- **语言与后端**：Python, FastAPI, Uvicorn, Pydantic, Requests
- **AI 与数据**：DeepSeek API, 阿里云百炼 (DashScope), ChromaDB, Pandas, MySQL
- **前端与界面**：Gradio
- **工程与部署**：Docker, Docker Compose, Linux (云端部署)
