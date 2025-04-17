# .env loader setup
from dotenv import load_dotenv
load_dotenv()

# app.py
import streamlit as st
import time
from utils.extractors import extract_structured_data
from config.settings import get_openai_client
from schema.validation import validate_response, llm_response_schema

st.title("Clinical Note Wrangler")
st.markdown("Extract structured JSON data from messy clinical notes using LLMs.")

model = st.selectbox("Model", ["gpt-3.5-turbo", "gpt-4-turbo"])
temp = st.slider("Temperature", 0.0, 1.0, 0.9)
max_tokens = st.slider("Max Tokens", 100, 4096, 1400)

system_prompt = st.text_area(
    "System Prompt",
    """
You are a helpful assistant that extracts structured data in **valid JSON format** from messy clinical text notes.

Always return only a JSON object—no explanations, no extra text.

Use this JSON schema:

{
  "device": string,
  "mask_type": string (optional),
  "add_ons": [string] (optional),
  "qualifier": string (optional),
  "ordering_provider": string,
  "diagnosis": string (optional),
  "SpO2": string (optional),
  "usage": [string] (optional),
  "type": string (optional),
  "features": [string] (optional),
  "mobility_status": string (optional),
  "product": string (optional),
  "components": [string] (optional),
  "compliance_status": string (optional)
}

Only include fields relevant to the note. Omit fields not mentioned.
"""
)

user_prompt = st.text_area("User Prompt", "Paste your input clinical note here.")

if st.button("Extract JSON"):
    client = get_openai_client()
    with st.spinner("Extracting..."):
        start_time = time.time()
        try:
            result, usage = extract_structured_data(
                client=client,
                model=model,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                temperature=temp,
                max_tokens=max_tokens
            )
            is_valid, error = validate_response(result, llm_response_schema)
            end_time = time.time()

            if is_valid:
                st.subheader("Extracted JSON")
                st.code(result, language="json")
                st.markdown(f"**Tokens used:** {usage} | **Response time:** {end_time - start_time:.2f}s")
            else:
                st.error(f"Invalid JSON schema: {error}")

        except Exception as e:
            st.error(f"Error: {str(e)}")