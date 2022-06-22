# Exceptions

- keywords: Exceptions, Value Errors, Runtime Errors, try, else, pass

## Types of errors

- Errors in Python:
  - Syntax Errors
    - Unconditionally fatal

    ```
    >>> while True print('Hello world')
    SyntaxError: invalid syntax
    ```

  - Exceptions
    - Runtime error
    - Code is syntactically correct
    - Error is not unconditionally fatal
    - If not handled, result in an error message
    - Examples of exception names:
      - ZeroDivisionError
      - NameError
      - TypeError
      - ValueError
    - Standard exception names are built-in identifiers (not reserved keywords).

    ```
    >>> 10 * (1/0)
    ZeroDivisionError: division by zero
    ```
    ```
    >>> 4 + spam*3
    NameError: name 'spam' is not defined
    ```
    ```
    >>> '2' + 2
    TypeError: can only concatenate str (not "int") to str
    ```

## `try`

```python
try:
    x = int(input("What's x?"))
    printf(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

- If an exception occurs which does not match the exception named in the _except
  clause_, it is passed on to outer `try` statements; if no handler is found, it
  is an _unhandled exception_ and execution stops with a message as shown above.

- A `try` statement may have more than one _except clause_, to specify handlers
  for different exceptions. At most one handler will be executed. Handlers only
  handle exceptions that occur in the corresponding _try clause_, not in other
  handlers of the same `try` statement. An except clause may name multiple
  exceptions as a parenthesized tuple, for example:

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

- Exception handlers don’t just handle exceptions if they occur immediately in
  the _try clause_, but also if they occur inside functions that are called
  (even indirectly) in the _try clause_. For example:


```python
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)  # Handling run-time error: division by zero
```


## else

```python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

- The use of the `else` clause is better than adding additional code to the
  `try` clause because it avoids accidentally catching an exception that wasn't
  raised by the code being protected by the `try … except` statement.


## Using try statement in a function

```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int()
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")


main()
```


## `pass`

- The pass statement does nothing.
- It can be used when a statement is required syntactically but the program
  requires no action.

```python
def initlog(*args):
    pass   # Remember to implement this!
```

```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt)
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
```


## Resources:

- [Python tutorial on Errors and Exceptions](https://.python.org/3/tutorial/errors.html)
- [`pass` statement](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)
- [List of built-in exceptions and their meanings](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)
  - Check for [Concrete exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)
- Helper functions for problem sets:
  - [dict.get()](https://docs.python.org/3/library/stdtypes.html#dict.get)
  - [list.index()](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
