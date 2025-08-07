from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI


load_dotenv()


llm = ChatOpenAI(model='gpt-4o-mini', temperature=1.5, max_completion_tokens=20)

result = llm.invoke('Talk me about bhubaneswar compared to batote.')

print(result.content)

