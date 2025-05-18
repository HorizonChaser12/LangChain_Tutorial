from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=1)

# Problem 1
# The problem with this loop is that it doesn't have contextual understanding or in short we can say it doesnt have Context memory of what it was asked in the previous prompt.
# while True:
#     user_input = input('You: ')
#     if user_input == ('exit'):
#         print("Okay, talk to you later on!")
#         break
#     result= model.invoke(user_input)
#     print("AI: ",result.content)


# Problem 2
# Another problem arises that all the data we are appending to the chat_history will eventually be high when we continue to talk more with the chatbot, and after a while it will be unable to find the difference between what chat is asked by us and what is answered by AI.
# chat_history = []
# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input == ('exit'):
#         print("Okay, talk to you later on!")
#         break
#     result= model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("AI: ",result.content)


# To mitigate that we are creating a dictionary which will store the data in key:value pairs where key will be the USER or AI and value will be the chat we both are talking about.
# Fortunately this was solved by Langchain, they have rendered what type of messages are there and how can you assign them with all those values.

chat_history = []
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == ('exit'):
        print("Okay, talk to you later on!")
        break
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
    
print(chat_history)