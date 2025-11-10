import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="ChatGPT Agent", page_icon="🤖", layout="centered")

st.title("ChatGPT Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini", 
                messages=st.session_state.messages,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
