from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI( base_url="https://api.deepseek.com",api_key= os.getenv("DEEPSEEK_API_KEY"))
prompt = [ {"role": "system", "content": "You are a helpful assistant."}]
print("Welcome to Deepseek Personal Agent. Type 'exit' to quit.")
while True:
    print()
    userInput = input("You : ")
    if userInput.lower() == "exit":
        print("Goodbye 👋")
        break  
    prompt.append({"role": "user", "content": userInput}) 
    response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=prompt,
                    temperature=0.7
                )
    
    reply = response.choices[0].message.content
    prompt.append({"role": "assistant", "content": reply})
    print("Agent :" ,reply)
