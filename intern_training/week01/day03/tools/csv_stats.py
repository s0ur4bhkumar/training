"""
cli tool for analysing csv files
"""

import argparse
from pathlib import Path

"""
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("--output", default="out.txt")
parser.add_argument("--verbose", action="store_true")
parser.add_argument("--count", type=int,default=5)
parser.add_argument("--timeout", type=int,default=10)
args = parser.parse_args()
print("Input:", args.input)
print("output:", args.output)
print(":", args.verbose)
"""

parser = argparse.ArgumentParser()
file = parser.add_argument("--file", required=True)
