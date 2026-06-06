import streamlit as st
import pandas as pd
from services.profiler import get_profile
from services.insight_engine import generate_insights
from services.story_generator import generate_story

st.set_page_config(page_title="Data Storytelling Copilot", layout="wide")

st.title("📊 Data Storytelling Copilot (SLM Powered)")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    profile = get_profile(df)

    c1, c2, c3 = st.columns(3)
    c1.metric("Rows", profile["rows"])
    c2.metric("Columns", profile["columns"])
    c3.metric("Missing Values", profile["missing"])

    insights = generate_insights(df)

    st.subheader("Insights")
    for insight in insights:
        st.write("✅", insight)

    if st.button("Generate Executive Summary"):
        with st.spinner("Generating story..."):
            summary = generate_story(insights)

        st.subheader("Business Story")
        st.write(summary)
