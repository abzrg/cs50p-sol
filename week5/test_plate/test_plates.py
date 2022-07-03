"""
----------------------------
Re-requesting a Vanity Plate
----------------------------

It is assumed that the user enter all alphabetic
characters as uppercase, so no need to test for it.

Source: https://cs50.harvard.edu/python/2022/psets/5/test_plates/
"""

from plates import is_valid


def test_start_two_letter():
    """
    All vanity plates must start with at least two letters
    """
    assert is_valid("1") is False
    assert is_valid("23") is False
    assert is_valid("AB") is True
    assert is_valid("CS50") is True
    assert is_valid("355F") is False


def test_length():
    """
    Max: 6
    Min: 2
    """
    assert is_valid("C") is False  # len < 2
    assert is_valid("CS") is True  # len == 2
    assert is_valid("CS50") is True  # 2 < len < 6
    assert is_valid("CS5012") is True  # len == 6
    assert is_valid("CS50123") is False  # len > 6


def test_number_in_middle():
    """
    Numbers cannot be used in the middle of a plate
    """
    assert is_valid("AAA222") is True
    assert is_valid("AAA22A") is False


def test_first_number_zero():
    """
    To first number cannot be zero
    """
    assert is_valid("CS50") is True
    assert is_valid("CS05") is False


def test_period_space_punctuation():
    """
    No periods, spaces, or punctuation marks are allowed
    """
    assert is_valid("PI3.14") is False
    assert is_valid("PI3 14") is False
    assert is_valid("PI3?14") is False
