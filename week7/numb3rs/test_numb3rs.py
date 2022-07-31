"""\
------------
TEST NUMB3RS
------------

Test numbers.py functions

Source: https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
"""

from numb3rs import validate


def test_non_digit():
    assert validate("cat") is False
    assert validate("cat.dog.bird.fly") is False


def test_digits_in_range():
    assert validate("-1.-1.-1.-1") is False
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("256.256.256.256") is False
    assert validate("1000.1000.1000.1000") is False


def test_ipv4_format():
    assert validate("0") is False
    assert validate("1.") is False
    assert validate("1.2") is False
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") is False
    assert validate("1..2.3") is False
    assert validate("1...2") is False
