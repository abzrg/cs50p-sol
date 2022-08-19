"""\
Tests for seasons.py
"""

from seasons import validate

def test_range() -> None:
    assert validate("10000-01-02") is False
    assert validate("1999-13-02") is False
    assert validate("1999-12-32") is False
    assert validate("1999-11-22") is True


def test_without_dash() -> None:
    assert validate("1990 01 01") is False
    assert validate("19991119") is False


def text_non_numerical() -> None:
    assert validate("January 1, 1999") is False
