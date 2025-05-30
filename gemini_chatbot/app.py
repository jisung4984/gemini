import streamlit as st
import google.generativeai as genai
from typing import List

# Gemini API 설정
genai.configure(api_key=st.secrets["gemini"]["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# 세션 상태 초기화
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

# 제목 설정
st.title("Gemini AI Chatbot")

# 채팅 히스토리 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요"):
    # 사용자 메시지 표시
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Gemini 응답 생성
        response = st.session_state.chat.send_message(prompt)
        
        # 응답 표시
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}") 