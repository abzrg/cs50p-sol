import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(10)
    assert jar.capacity == 10


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.deposit(11)
    jar = Jar(2)
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(10)
    jar.withdraw(10)
    assert jar.size == 0
