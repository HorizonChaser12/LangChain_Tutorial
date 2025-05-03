from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm =  HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-235B-A22B",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What does the name 'Suryakanta' means?")

print(result.content)