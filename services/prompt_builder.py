def build_prompt(
    df,
    user_question
):

    columns = "\n".join(
        [
            f"{col} ({df[col].dtype})"
            for col in df.columns
        ]
    )

    sample = df.head(20).to_string()

    return f"""
You are a senior business analyst.

Dataset Columns:

{columns}

Dataset Sample:

{sample}

Question:

{user_question}

Provide a clear business response.
"""