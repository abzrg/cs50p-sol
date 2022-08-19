"""\
----------
Cookie Jar
----------

Implementation of a Cookie Jar

Source: https://cs50.harvard.edu/python/2022/psets/8/jar/
"""


class Jar:
    def __init__(self, capacity: int = 12) -> None:
        self.capacity = capacity
        self.size = 0

    def __str__(self) -> str:
        return "🍪" * self.size

    def deposit(self, n: int) -> None:
        self.size += n

    def withdraw(self, n: int) -> None:
        self.size -= n

    @property
    def capacity(self) -> int:
        """Maximum number of cookies that can fit in the cookie jar."""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if size < 0:
            raise ValueError("There is not enough cookies.")
        if size > self.capacity:
            raise ValueError("There is not enough space.")
        self._size = size
