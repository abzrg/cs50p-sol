# Week 2: Loops

- **keywords**: while, for, list, range(), break (in conjunction with an infinite
  loop), len(), dict, none

- If a variable (especially in loops) has no purpose in the program it is
  usually renamed to `_`.

- pythonic

```python
print("meow\n" * 3, end="")

# meow
# meow
# meow
```

## `range()`

```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
```


## Length

```python
students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, student[i])
```


## dict

- dicts or dictionaries is a data structure that allows you to associate keys
  with values.

```python
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student])
```

- list of dictionaries:

```python
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
```
  - Python has a special None designation where there is no value associated with a key.


## Misc. notes

- Python recommends **snake case**.

## Resources:

- [Introduction to lists](https://www.oreilly.com/content/how-do-i-use-the-slice-notation-in-python/)
- [Documentation of lists](https://docs.python.org/3/tutorial/datastructures.html)
  - Methods
  - List comprehension
- [Python \[\] slice notation](https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html)
  - Note the notation for getting reverse of a list
  - Also check [this](https://www.oreilly.com/content/how-do-i-use-the-slice-notation-in-python/)
- [Python's documentation on len()](https://docs.python.org/3/library/functions.html?highlight=len#len)
- [Python's documentation on range()](https://docs.python.org/3/library/stdtypes.html#range)
- [Python's documentation on dict()](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
