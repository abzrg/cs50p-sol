"""
-------
Refueling
-------


Source: https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
"""

import pytest
from fuel import convert, gauge

def test_convert_zero_division():
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_frac_above_100():
    with pytest.raises(ValueError):
        convert("100/3")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percent():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
