import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
prompt = [ {"role": "system", "content": "You are a helpful assistant."}]
print("Welcome to ChatGPT Personal Agent. Type 'exit' to quit.")
while True:
    print()
    userInput = input("You : ")
    if userInput.lower() == "exit":
        print("Goodbye 👋")
        break  
    prompt.append({"role": "user", "content": userInput}) 
    response = client.chat.completions.create(
                    model="gpt-4o-mini", 
                    messages=prompt,
                    temperature=0.7
                )
    
    reply = response.choices[0].message.content
    prompt.append({"role": "assistant", "content": reply})
    print("Agent :" ,reply)
