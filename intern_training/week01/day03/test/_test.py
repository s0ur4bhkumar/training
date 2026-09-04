"""
Testing module
"""

from energy_insights.daily_average import compute_daily_averages
from energy_insights.find_spikes import find_spikes

sample_rows = [
    {"timestamp": "2026-03-01 08:30:00", "price": "100.50"},
    {"timestamp": "2026-03-01 14:15:00", "price": "105.00"},
    {"timestamp": "2026-03-01 18:45:00", "price": "99.00"},
    {"timestamp": "2026-03-02 09:10:00", "price": "110.25"},
    {"timestamp": "2026-03-02 16:20:00", "price": "115.75"},
    {"timestamp": "2026-03-03 11:00:00", "price": "102.00"},
]


def test_compute_daily_averages():
    """
    test for daily_average module
    """
    assert compute_daily_averages(
        rows=sample_rows, ts_col="timestamp", value_col="price"
    ) == {"2026-03-01": 101.5, "2026-03-02": 113.00, "2026-03-03": 102.00}


def test_find_spike():
    """
    test for find_spike module
    """
    assert find_spikes(rows=sample_rows, value_col="price", top=3) == [
        {"timestamp": "2026-03-02 16:20:00", "price": "115.75"},
        {"timestamp": "2026-03-02 09:10:00", "price": "110.25"},
        {"timestamp": "2026-03-01 14:15:00", "price": "105.0"},
    ]


def test_main():
    """
    test for main cli application
    """
