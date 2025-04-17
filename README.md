# Clinical Note Wrangler

A lightweight LLM-powered app to extract structured JSON from messy clinical notes.

## Setup

```bash
git clone https://github.com/your-org/clinical-note-wrangler.git
cd clinical-note-wrangler
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=sk-...
```

## Run the App

```bash
streamlit run app.py
```

## Features

- Prompt input
- Model + parameter control
- JSON output with validation
- Token + time tracking

## For the DME Healthcare Team

Tweak system prompts to better extract fields like device, diagnosis, SpO2, usage, etc.

## Application UI
![image](https://github.com/user-attachments/assets/704942c5-87e5-4f1e-bcb3-caac104a8a1f)

---

Want to deploy or integrate with LangChain? Just ask!
