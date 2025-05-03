from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# # Retrieve the Gemini API key
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if GEMINI_API_KEY is None:
#     raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro',temperature=0.7)

# Generate a response
result = llm.invoke("How biased can you be?")

# Output the result
print(result.content)
