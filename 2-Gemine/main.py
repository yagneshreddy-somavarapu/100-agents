from dotenv import load_dotenv
import google.generativeai as genai
import os


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.0-flash")

print("Welcome to Gemini Chat Agent! Type 'exit' to quit.\n")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break 
    response = model.generate_content(user_input)
    print("Agent:", response.text)