from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# You should leaen streamlit, pretty handtool to get a good UI.
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',temperature=0.7)
 
st.header("Research Tool")

paper_input = st.selectbox( "Select Research Paper Name",["Select from the drop down..","Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] ) 

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-S paragraphs)", "Long (detailed explanation)"] ) 


# Here we are actually sending this template to the LLM rather than the user query. This is called Dynamic Prompting.
# The main differnce it creates than that of Static Prompting is that it doesn't give unrelated data as well as its correctness is also examined.
# We are using this load prompt to help mitigate the reuse of templates whenever necessary, we can just call this method in that place.

template = load_prompt("4.Prompts/Template.json")

prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)        