from openai import OpenAI

# 1. 初始化客户端，把地址指向 DeepSeek
client = OpenAI(
    api_key="sk-48cf683bfa944be6a4bdecaf51f0f564", # ⚠️ 这里换成你自己的 Key！
    base_url="https://api.deepseek.com"
)

# 2. 发送对话请求
response = client.chat.completions.create(
    model="deepseek-chat", # 指定使用的模型
    messages=[
        {"role": "system", "content": "你是一个二手车评估专家。"}, # 设定人设
        {"role": "user", "content": "给我找一下十五万左右的suv，有什么建议？"} # 用户的问题
    ]
)

# 3. 打印大模型的回答
print(response.choices[0].message.content)