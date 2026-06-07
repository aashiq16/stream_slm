import requests
import streamlit as st

API_KEY = st.secrets["OLLAMA_API_KEY"]
API_ENDPOINT = st.secrets["API_ENDPOINT"]

def ask_slm(prompt):

    response = requests.post(
        API_ENDPOINT,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]
