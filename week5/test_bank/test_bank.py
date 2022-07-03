"""
----------------
Back to the Bank
----------------

Test value of the greeting


Source: https://cs50.harvard.edu/python/2022/psets/5/test_bank/
"""

from bank import value


def test_h():
    """h at the beginning"""
    assert value("hi!") == 20
    assert value("hallo") == 20
    assert value("hello") == 0


def test_hello():
    """hello at the beginning"""
    assert value("hello") == 0
    assert value("hello hello") == 0
    assert value("hello") == 0
    assert value("hello") == 0


def test_numbers():
    """Numbers in the beginning"""
    assert value("123 hello") == 100


def test_punc():
    """Punctuation at the beginnig"""
    assert value("! hello") == 100
    assert value("., hello!") == 100


def test_upper():
    """Starting with uppercase"""
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hallo") == 20
    assert value("BONJOUR") == 100
