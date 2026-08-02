import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage ,
    HumanMessage ,
    AIMessage 
)
model = ChatMistralAI(model="mistral-small-2506", temperature=0.7, max_tokens=512)
print("-----------type 0 , if you want to exit the chat-----------")

messages = [SystemMessage(content="You are a funny AI agent.")
] 
while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        print("Chat ended. 👋")
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:", response.content)

print(messages)
print("\n------ Chat History ------")
for msg in messages:
    print(f"{type(msg).__name__}: {msg.content}")
    