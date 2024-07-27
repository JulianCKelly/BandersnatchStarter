from pandas import DataFrame
from altair import Chart


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    result = (Chart(df, title=f"{y} by {x} for {target}").mark_circle()
               .encode(x=x, y=y, color=target).interactive())

    return result
