import streamlit as st
import google.generativeai as genai

# 페이지 기본 설정
st.set_page_config(
    page_title="Gemini 챗봇",
    page_icon="🤖",
    layout="wide"
)

# Gemini API 키 확인 및 초기화
if not st.secrets["gemini"]["GOOGLE_API_KEY"]:
    st.error("🚨 Google API 키가 설정되지 않았습니다. .streamlit/secrets.toml 파일에 API 키를 설정해주세요.")
    st.stop()

# Gemini 모델 초기화
try:
    genai.configure(api_key=st.secrets["gemini"]["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error(f"🚨 Gemini API 초기화 중 오류가 발생했습니다: {str(e)}")
    st.stop()

# 제목과 설명
st.title("Gemini 챗봇")
st.markdown("Gemini API를 활용한 기본 챗봇 프레임워크입니다.")

# 세션 상태 초기화
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 이전 대화 내용 표시 (Expander 사용)
with st.expander("이전 대화 보기", expanded=False):
    if not st.session_state.chat_history:
        st.info("아직 대화 내역이 없습니다.")
    else:
        for i, message in enumerate(st.session_state.chat_history):
            # 메시지 구분선 추가 (첫 메시지 제외)
            if i > 0:
                st.divider()
            
            # 발신자 표시 (사용자/AI)
            sender = "🧑 사용자" if message["role"] == "user" else "🤖 Gemini"
            st.caption(sender)
            
            # 메시지 내용 표시
            st.markdown(message["content"])

# 현재 대화 표시
st.markdown("### 현재 대화")
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력해주세요..."):
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 사용자 메시지를 채팅 히스토리에 추가
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    try:
        # Gemini API로 응답 생성
        with st.chat_message("assistant"):
            with st.spinner("응답을 생성하고 있습니다..."):
                response = st.session_state.chat.send_message(prompt)
                st.markdown(response.text)
                
                # AI 응답을 채팅 히스토리에 추가
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
    
    except Exception as e:
        st.error(f"응답 생성 중 오류가 발생했습니다: {str(e)}")
        # 오류 메시지를 채팅 히스토리에 추가
        st.session_state.chat_history.append({"role": "assistant", "content": f"🚨 오류: {str(e)}"}) 