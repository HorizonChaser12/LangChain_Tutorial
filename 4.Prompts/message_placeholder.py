# A MessagePlaceholder in LangChain is a special placeholder used inside a ChatPromptTemplateto dynamically insert chat history or a list of messages at runtime.
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

# process of creating it: 1- Chat template , 2- Load Chat history, 3- create prompt with the chat history within it.

# Chat Template
chat_template =  ChatPromptTemplate([
    ('system','You are a intelligent customer support agent'),
    # This acts as a bridge to the previous conversation you had with the AI.
    MessagesPlaceholder(variable_name='chat_history')
    ('human','{query}')   
])

# Load Chat History
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)    

# Creat prompt to invoke whatever we have created till now.
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my order or when can I get the refund?'})
print(prompt)