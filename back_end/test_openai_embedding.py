import openai

# 设置 API Key，申请地址：https://platform.openai.com/account/api-keys
openai.api_key = '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' 
# 设置组织，查看地址：https://platform.openai.com/account/org-settings
openai.organization = "org-jy2eL6AhJYOSnDydGNQpPcro"

EMBEDDING_DIM = 1536
model = "text-embedding-ada-002"
text = "Hello World."

result = openai.Embedding.create(
    model=model,
    input=text
)

print(result['data'][0]['embedding'])