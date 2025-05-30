import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(
    page_title="Gemini 챗봇",
    page_icon="🤖",
    layout="wide"
)

# Gemini API 설정
api_key = st.secrets["gemini"]["api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# 제목
st.title("💬 Gemini-1.5-Flash 챗봇")
st.markdown("Gemini API를 활용한 대화형 챗봇입니다.")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 채팅 기록 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요..."):
    # 사용자 메시지 추가
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI 응답 생성
    with st.chat_message("assistant"):
        context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
        response = model.generate_content([context, prompt])
        assistant_reply = response.text.strip()
        st.markdown(assistant_reply)
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

# 사이드바에 대화 초기화 버튼 추가
with st.sidebar:
    if st.button("🔄 대화 초기화", use_container_width=True):
        st.session_state.messages = []
        st.rerun() 
