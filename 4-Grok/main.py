import os
from xai_sdk import Client
from xai_sdk.chat import user, system
from dotenv import load_dotenv
load_dotenv()

client = Client(api_key=os.getenv("XAI_API_KEY"), timeout=3600)
chat = client.chat.create(model="grok-4")  
chat.append(system("You are Grok, a helpful assistant."))
while True:
    chat = input("You : ")
    if chat.lower() == "exit":
        print("Goodbye 👋")
        break
    chat.append(user(chat))
    response = chat.sample()
    print("Grok : ", response.content)

