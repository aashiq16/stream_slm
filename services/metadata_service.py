import pandas as pd


def get_metadata(df):

    metadata = []

    for col in df.columns:

        metadata.append(
            {
                "column": col,
                "type": str(df[col].dtype),
                "nulls": int(df[col].isnull().sum())
            }
        )

    return metadata


def get_dataset_summary(df):

    summary = {

        "rows": len(df),

        "columns": len(df.columns),

        "missing_values": int(
            df.isnull().sum().sum()
        ),

        "column_names": list(df.columns)
    }

    return summary


def get_numeric_columns(df):

    return list(
        df.select_dtypes(
            include=["int64", "float64"]
        ).columns
    )


def get_text_columns(df):

    return list(
        df.select_dtypes(
            include=["object"]
        ).columns
    )


def build_dataset_context(df):

    context = []

    context.append(
        f"Rows: {len(df)}"
    )

    context.append(
        f"Columns: {len(df.columns)}"
    )

    context.append(
        f"Missing Values: {df.isnull().sum().sum()}"
    )

    context.append("\nColumns:\n")

    for col in df.columns:

        context.append(
            f"- {col} ({df[col].dtype})"
        )

    return "\n".join(context)