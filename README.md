# Clinical Note Wrangler

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-blueviolet)](https://platform.openai.com/docs)

A lightweight LLM-powered app to extract structured JSON from unstructured clinical notes.

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
