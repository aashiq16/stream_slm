import pandas as pd


def generate_insights(df):

    insights = []

    numeric_cols = df.select_dtypes(
        include="number"
    )

    for col in numeric_cols.columns:

        max_value = df[col].max()
        min_value = df[col].min()
        avg_value = df[col].mean()

        insights.append(
            f"{col} maximum value is {max_value:,.2f}"
        )

        insights.append(
            f"{col} average value is {avg_value:,.2f}"
        )

        if len(df) > 1:

            start = df[col].iloc[0]
            end = df[col].iloc[-1]

            if start != 0:

                growth = (
                    (end - start)
                    / start
                ) * 100

                insights.append(
                    f"{col} changed by {growth:.2f}%"
                )

        if max_value > (avg_value * 1.5):

            insights.append(
                f"{col} contains a possible spike"
            )

        if min_value < (avg_value * 0.5):

            insights.append(
                f"{col} contains a possible drop"
            )

    return insights