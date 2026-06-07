def get_profile(df):

    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing": int(df.isnull().sum().sum()),
        "column_names": list(df.columns)
    }

    return profile