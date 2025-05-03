from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables
load_dotenv()

# Retrieve the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

# Initialize the Gemini LLM
llm = GoogleGenerativeAI(model='gemini-1.5-flash', api_key=GEMINI_API_KEY)

# Generate a response
result = llm.invoke("What is the capital of India?")

# Output the result
print(result)
# result.content only outputs the answer or response given by the llm rather than showing all the metadata.
