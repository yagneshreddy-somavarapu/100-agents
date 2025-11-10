

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config(page_title="Gemini Chat Agent", page_icon="🤖", layout="centered")
st.title("Gemini Chat Agent")


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if prompt := st.chat_input("Say something..."):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
