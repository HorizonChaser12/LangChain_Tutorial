from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import logging

# Enable debugging for Google API requests
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("google").setLevel(logging.DEBUG)

# Load the .env file where the API keys are stored
load_dotenv()

# Specify the correct model name for embeddings
# The models/ prefix killed my 30 mins for the debugging
embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

# The data from which our query will be answered
documents = [
    "Rahul is a Full Time Employee in TCS",
    "Kiran kumar Sahoo is a Full Time Employee in Piescon Software Company",
    "Sadhuram raman Lenka is a Full Time Employee in HighRadius"
]

# User query
query = "Tell me about Lenka."

# Generate embeddings
doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

# Calculate cosine similarity
scores = cosine_similarity([query_embeddings], doc_embeddings)

# Find the most similar document
index = np.argmax(scores)

print('The user query was:', query)
print('The output answer is:', documents[index])
print('The similarity is:', scores[0][index])