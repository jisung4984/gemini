# Gemini Chatbot

Streamlit 기반의 Gemini AI 챗봇 애플리케이션입니다.

## 설치 방법

1. 저장소 클론:
```bash
git clone https://github.com/jisung4984/gemini.git
cd gemini
```

2. 가상환경 생성 및 활성화:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

4. Gemini API 키 설정:
- `.streamlit/secrets.toml` 파일을 생성하고 다음 내용을 추가:
```toml
[gemini]
GOOGLE_API_KEY = "your-api-key-here"
```

## 실행 방법

```bash
streamlit run app.py
```

또는 `run_app.bat` 파일을 실행하세요.

## 기능

- Gemini AI와의 실시간 대화
- 대화 히스토리 저장 및 조회
- 사용자 친화적인 인터페이스 