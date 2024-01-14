from pandas import DataFrame
from altair import Chart, Tooltip


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:

    properties = {
        'width': 600,    # Set the desired width of the chart
        'height': 400,   # Set the desired height of the chart
        'background': '#1E1E1E',  # Dark background color to fit Bandersnatch theme
        'padding': {'left': 20, 'right': 20, 'top': 10, 'bottom': 10}  # Adjust padding as needed
    }
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}", properties=properties
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).configure_title(fontSize=20, color='#FFFFFF')

    return graph


