"""
----------------
Testing my twttr
----------------

Tests for shorten function

Source: https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
"""

from twttr import shorten


def test_empty():
    """
    Test that empty strings are handled correctly.
    """
    assert shorten("") == ""


def test_numbers():
    """
    Test that numbers are handled correctly
    """
    assert shorten("123") == "123"


def test_punc():
    """
    Test that punctuation is handled correctly.
    """
    assert shorten("!@#") == "!@#"


def test_consonants():
    """
    Test that consonants are handled correctly.
    """
    assert shorten("qwrty") == "qwrty"
    assert shorten("dvrk") == "dvrk"
    assert shorten("clmk") == "clmk"


def test_vowels():
    """
    Test that vowels are handled correctly.
    """
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
