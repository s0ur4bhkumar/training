import pandas as pd


def malformed_check(file_path: str, value_col: str):
    missing_values = ["n/a", "na", "--"]
    df = pd.read_csv(file_path, na_values=missing_values)
    if value_col not in df.columns:
        f"column {value_col} not available in dataset"
        return True
    for value in df[value_col].isnull():
        if value is True:
            print("bad dataset, please clean the data")
            return True


print(
    malformed_check(
        file_path="./malformed_temperature_dataset.csv", value_col="temperature"
    )
)
