import plotly.express as px


def create_line_chart(
        df,
        x_col,
        y_col
):

    fig = px.line(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} Trend"
    )

    return fig