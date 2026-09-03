"""
main file for package
"""

import sys

from energy_insights import csv_stats

if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print("""
        a set of csv handling tools
        """)

sample_rows = [
    {"timestamp": "2026-03-01 08:30:00", "price": "100.50"},
    {"timestamp": "2026-03-01 14:15:00", "price": "105.00"},
    {"timestamp": "2026-03-01 18:45:00", "price": "99.00"},
    {"timestamp": "2026-03-02 09:10:00", "price": "110.25"},
    {"timestamp": "2026-03-02 16:20:00", "price": "115.75"},
    {"timestamp": "2026-03-03 11:00:00", "price": "102.00"},
]


def csv_summary():
    print(csv_stats)
