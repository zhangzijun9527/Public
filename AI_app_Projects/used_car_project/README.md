# 🚗 二手车 AI 智能评估与检索系统 (Used Car AI RAG Platform)

这是一个基于真实二手车脏数据构建的**全栈式 AI 应用**。项目打通了从数据清洗、关系型数据库存储、向量语义检索、大模型生成到前端可视化交互的完整数据闭环。

## 📸 产品展示 (UI Demo)
![Gradio 前端界面](ui_demo.png)

## 🏗️ 核心架构 (Architecture)
1. **数据清洗层**：使用 `Pandas` 对原始二手车 CSV 进行异常值处理与缺失值填充，并将干净数据持久化至 `MySQL`。
2. **向量检索层**：引入 `ChromaDB` 向量数据库与 `BAAI/bge-small-zh-v1.5` 中文 Embedding 模型，实现基于语义的精准知识检索。
3. **后端服务层**：基于 `FastAPI` 提供 RESTful API，并利用 `SQLAlchemy` 进行数据持久化交互。
4. **大模型生成层**：无缝接入 `DeepSeek API`，通过 Prompt 上下文注入（RAG 架构），有效解决大模型幻觉，实现可溯源的智能问答。
5. **前端交互层**：使用 `Gradio` 搭建极简聊天界面，支持多轮对话与参考来源同步展示。

## 🛠️ 技术栈 (Tech Stack)
- **语言**: Python 3.13
- **数据处理**: Pandas, NumPy
- **数据库**: MySQL, SQLAlchemy
- **AI / RAG**: DeepSeek API, ChromaDB, Sentence-Transformers
- **Web 框架**: FastAPI, Uvicorn, Gradio

## 🚀 快速开始 (Quick Start)
1. 安装依赖：
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql openai chromadb sentence-transformers gradio requests
