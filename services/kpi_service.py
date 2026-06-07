def generate_kpis(df):

    kpis = {}

    numeric_cols = df.select_dtypes(
        include="number"
    )

    for col in numeric_cols.columns:

        kpis[col] = {
            "max": float(df[col].max()),
            "avg": float(df[col].mean()),
            "min": float(df[col].min())
        }

    return kpis