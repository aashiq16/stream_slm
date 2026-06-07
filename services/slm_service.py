import requests
import streamlit as st

API_KEY = st.secrets["OLLAMA_API_KEY"]

MODEL_NAME = "gemma3:4b"


def ask_slm(prompt):

    response = requests.post(
        "https://ollama.com/api/chat",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": """
You are Daily Data Partner, a Senior Data Analyst.

Your responsibilities:
- Analyze datasets objectively.
- Generate executive summaries.
- Identify trends and patterns.
- Highlight risks and opportunities.
- Use business-friendly language.
- Present insights in bullet points.
- Focus on actionable recommendations.
- Never mention that you are an AI.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]
