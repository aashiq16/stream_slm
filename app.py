
import streamlit as st

from services.data_loader import load_csv
from services.metadata_service import get_metadata
from services.story_generator import ask_dataset


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    layout="wide"
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("📊 Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )

    if uploaded_file:

        df = load_csv(uploaded_file)

        st.session_state["df"] = df

        st.success("Dataset Loaded")

        st.divider()

        st.subheader("Dataset Metadata")

        st.write(
            f"Rows: {len(df):,}"
        )

        st.write(
            f"Columns: {len(df.columns)}"
        )

        st.write(
            f"Missing Values: {df.isnull().sum().sum():,}"
        )

        st.divider()

        st.subheader("Column Explorer")

        metadata = get_metadata(df)

        for item in metadata:

            with st.expander(
                item["column"]
            ):

                st.write(
                    f"Type: {item['type']}"
                )

                st.write(
                    f"Null Values: {item['nulls']}"
                )

# ==========================================
# MAIN PAGE
# ==========================================
st.title("📈Daily Data Partner")

st.caption(
    "Upload a dataset and ask questions in natural language."
)

# ==========================================
# NO DATA UPLOADED
# ==========================================

if "df" not in st.session_state:

    st.info(
        "Upload a CSV dataset from the sidebar to begin."
    )

    st.subheader("Example Questions")

    st.markdown("""
- Give me an executive summary

- What are the key observations?

- Explain this dataset to leadership

- What trends stand out?

- What risks should management know?

- Identify opportunities

- Create a CEO briefing

- Summarize business performance
""")

# ==========================================
# DATA LOADED
# ==========================================

else:

    df = st.session_state["df"]

    # Initialize Chat

    if "messages" not in st.session_state:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content":
                f"""
Dataset loaded successfully.

Rows: {len(df):,}

Columns: {len(df.columns)}

Available Fields:

{', '.join(df.columns)}

Ask me anything about your data.
"""
            }
        ]

    # Display Chat History

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    # Chat Input

    user_prompt = st.chat_input(
        "Ask anything about your dataset..."
    )

    if user_prompt:

        # User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(
                user_prompt
            )

        # Assistant Response

        with st.chat_message("assistant"):

            with st.spinner(
                "Analyzing dataset..."
            ):

                try:

                    response = ask_dataset(
                        df,
                        user_prompt
                    )

                except Exception as e:

                    response = (
                        f"Error: {str(e)}"
                    )

                st.markdown(
                    response
                )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )