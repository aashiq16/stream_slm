import requests
import streamlit as st

API_KEY = st.secrets["OLLAMA_API_KEY"]

response = requests.get(
    "https://ollama.com/v1/models",
    headers={
        "Authorization": f"Bearer {API_KEY}"
    }
)

st.write("Status:", response.status_code)
st.write(response.text)
