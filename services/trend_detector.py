def detect_trends(df):

    trends = []

    numeric_cols = df.select_dtypes(
        include="number"
    )

    for col in numeric_cols.columns:

        start = df[col].iloc[0]
        end = df[col].iloc[-1]

        if end > start:

            trends.append(
                f"{col} shows an upward trend."
            )

        elif end < start:

            trends.append(
                f"{col} shows a downward trend."
            )

        else:

            trends.append(
                f"{col} remains stable."
            )

    return trends