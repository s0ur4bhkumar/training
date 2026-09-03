"""
cli tool for analysing csv files
"""

import argparse
import sys
from pathlib import Path
from typing import Protocol

import pandas as pd


def help():
    print("""
   A cli tool which gives basic stats of a csv file

     Arguments of cli:

     --file: name of the file to be analyzed (not optional)
     --top: for view only top n files,by default it will return all the rows (type:int, optional)
     --column: name of the column to be analyzed (not optional)

     use case:

     - python3 tools/csv_stats.py --file="hourly_prices.csv" --column=price --top=5  #default arguments

     """)


for i in sys.argv:
    if i == "--help" or i == "-h":
        help()
        sys.exit(0)


class CLIargs(Protocol):
    """
    type interface for cli args
    """

    file: str
    top: int
    column: str


parser = argparse.ArgumentParser()
file = str(parser.add_argument("--file", default="../hourly_prices.csv"))
n = parser.add_argument("--top", type=int, default=5)
column_name = parser.add_argument("--column", default="price")
args: CLIargs = parser.parse_args()  # pyright: ignore
base_dir = Path("../../")


try:
    file_name: str = args.file
    column: str = args.column
    top_n: int = args.top
    file_path = ""
    for path in base_dir.rglob(file_name):
        file_path = path
    with open(file_path, encoding="utf-8") as file:
        df: pd.DataFrame = pd.read_csv(file)
        # print(tabulate(df[column].head(top_n), tablefmt="fancy_grid"))
        print("\n")
        print("number of rows:", len(df))
        print("\n")
        print(f"top {top_n} rows of column {column}")
        print("\n")
        print(df[column].head(top_n))
        print("\n")
        print(f"{column} summary")
        print("\n")
        print("mean: ", round(df[column].mean(), 2))
        print("max: ", df[column].max())
        print("min: ", df[column].min())
except FileNotFoundError:
    print("invalid file name,check if the file is present in the given data directory")
