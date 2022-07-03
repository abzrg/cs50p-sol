# Unit Tests

## Outline

- Unit test
- `assert`
- `pytest`
- Testing Strings
- Organizing Tests into Folders



## Unit Tests

- Unit testing is a software development process in which the smallest
  testable parts of an application, called units, are individually and
  independently scrutinized for proper operation.[^1]

[^1]: https://www.techtarget.com/searchsoftwarequality/definition/unit-testing

- It's called unit testing because you break down the functionality of
  your program into discrete testable behaviors that you can test as
  individual units.[^2]

[^2]: https://docs.microsoft.com/en-us/visualstudio/test/unit-test-basics

- Convention:
  - Name of the test file: `test_libname.py`
  - Name of the units (e.g., functions): `test_funcname`

- Each test file need to have a `main` function and it should be
  called like following:

```python
# ~~~

if __name__ == "__main__":
    main()
```

  - This means, only call `main()` function when you run this file
    directly. Python interpreter sets the value of the special
    variable `__name__` to `__main__` for the file it is passed
    directly on the command-line. With this when one import this file,
    it is not going to call `main` function.

- Using `if` statement make our test file very soon bloated!

```python
def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
```


## `assert`

- [Documentation](https://docs.python.org/3/reference/simple_stmts.html#assert)
- The assert keyword is used when debugging code [^3].

[^3]: https://www.w3schools.com/python/ref_keyword_assert.asp

- The assert keyword lets you test if a condition in your code returns
  `True`, if not, the program will raise an `AssertionError`.

```python
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye"
```

- You can write a message to be written if the code returns `False`,
  check the example below.

```python
x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
```

or like this [^4]:

```python
number = 42

assert number > 0 and isinstance(number, int), \
    f"number greater than 0 expected, got: {number}"
```
[^4]: https://realpython.com/python-assert-statement/


### `__debug__` and `AssertionError`

- According to Python's documentation, assert is equivalent to the
  following:

```python
assert experssion1, expression2
if __debug__:
    if not expression1: raise AssertionError(expression2)
```

- In the current implementation, the built-in variable `__debug__` is
  `True` under normal circumstances, `False` when optimization is
  requested (command line option `-O`).


## Pytest

- [Documentation](https://docs.pytest.org/en/7.1.x/getting-started.html)

- pytest
- capsys, capsysf -- capture stdout


- Understand the output of pytest:

  - `F`: something in your code failed.
  - `.`: your code passed
  - `E`: provides some hints about the errors in your main code.

- Notice there is no need for a `main()` function:

```python
from calculator import square


def test_assert():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
```

- We can divide our test into different groups of tests:
  - One of the motivation for this is that if you put all your test under one test function, then you will not be able to see all failures in your test, as pytest stops checking after the first failure in the test function.
  - More error output allows you to further explore what might be producing the problems within your code.


```python
from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
```


## Testing strings

- Try return string instead of printing it in the function, and let
  the _caller_ function (like `main`) handle printing the return value
  of the function.

- So change this:

```python
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()

```

to this:

```python
def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
```

So that you can test it like:

```python
from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"
```


## Organizing Tests into Folders

- If you have many files and many functions in each of them, then you can tidy your project folder and organize all your tests in a folder so that you can run a whole folder of test with a single command

- conventional name for test folder: `test`!

- You don't have to prepend test files in the `test` directory with `test_`.

```python
# test/hello.py

from hello import hello
  
  
def test_default():
    assert hello() == "hello, world"
  
  
def test_argument():
    assert hello("David") == "hello, David"
```

- pytest will not allow us to run tests as a folder simply with this file (or a whole set of files) alone without a special `__init__` file.


```
.
├── hello.py
└── test
    ├── __init__.py
    └── hello.py
```


- [Documentation](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html?highlight=folder#pytest-import-mechanisms-and-sys-path-pythonpath) on import mechanism