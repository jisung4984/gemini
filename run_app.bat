@echo off
echo Gemini Chatbot 실행하기
echo =====================

:: 가상환경 활성화
call .\venv\Scripts\activate.bat

:: Streamlit 앱 실행
python -m streamlit run app.py

pause 