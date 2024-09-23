# Imports the necessary modules
from pandas import DataFrame  # Pandas DataFrame is used for handling tabular data
from altair import Chart  # Altair is a library for creating declarative statistical visualizations


# Defines a function that creates an interactive Altair chart
def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """
    Creates an interactive scatter plot using Altair, with x and y axes
    and points colored based on the 'target' column.

    Parameters:
    df (DataFrame): The input data as a Pandas DataFrame
    x (str): The column name for the x-axis
    y (str): The column name for the y-axis
    target (str): The column name for coloring the points

    Returns:
    Chart: An Altair chart object with the scatter plot
    """
    # Creates a scatter plot with interactive capabilities using Altair
    result = (Chart(df, title=f"{y} by {x} for {target}")  # Define chart with title
              .mark_circle()  # Specify the mark type (circle for scatter plot)
              .encode(x=x, y=y, color=target)  # Encode the x, y axes, and color by 'target'
              .interactive())  # Adds interactivity (e.g., zoom, pan)
    # Returns the chart object
    return result

