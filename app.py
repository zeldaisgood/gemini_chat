import streamlit as st
import google.generativeai as genai
from typing import List, Dict

st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages: List[Dict[str, str]] = []

st.title("💬 Gemini Chatbot")
st.markdown("기본 Gemini 챗봇입니다.")

user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    st.session_state.messages.append({"role": "user", "parts": [user_input]})
    response = model.generate_content(st.session_state.messages)
    bot_reply = response.text
    st.session_state.messages.append({"role": "model", "parts": [bot_reply]})

for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["parts"][0]
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(content)


