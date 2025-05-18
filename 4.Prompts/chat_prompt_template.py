from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} assistant'),
#     HumanMessage(content='Explain in simple terms, what is {topic}')
# ])

# The output will be : 
# messages=[SystemMessage(content='You are a helpful {domain} assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is {topic}', additional_kwargs={}, response_metadata={})]
# There is still a problem in this, although this is a dynamic message for storing the messages between AI and User, the placeholders arent changed as per the user's entry and thus when referring the AI to get a hold of the previous messages, it will be unsuccessfull.

# To mitiage that we will be using a different format to get the things properly.

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Helicopter Shot'})

print(prompt)

# Now the output is like :
# messages=[SystemMessage(content='You are a helpful cricket expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is Helicopter Shot', additional_kwargs={}, response_metadata={})]

# As you can see the placeholder are correctly filled as per our requirement.