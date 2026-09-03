import pandas as pd


def find_spikes(
    rows: list[dict[str, str]], value_col: str, top: int
) -> list[dict[str, str]]:
    df = pd.DataFrame(rows)
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
    return df.nlargest(top, value_col).to_dict(orient="records")





