from statistics import mean, pstdev

import pandas as pd
from rich import print

from energy_insights.daily_average import compute_daily_averages


def anamoly_detection(
    rows: list[dict[str, str]], ts_col: str, value_col: str
) -> tuple[bool, pd.DataFrame] | bool:
    average = round(mean([float(i[value_col]) for i in rows]), 2)
    stdv = round(pstdev([float(i[value_col]) for i in rows]), 2)
    # result = {
    #     i["zscore"]: round((float(i[value_col]) - average) / stdv, 2) for i in rows
    # }
    for i in rows:
        i["z-score"] = round((float(i[value_col]) - average) / stdv, 2)

    df = pd.DataFrame(rows)
    outliers = df[df["z-score"].abs() > 3]
    if outliers.empty:
        return False
    return (True, outliers)
