## Singleton Comparison

- Problematic code [^1]
```python
foo = True
if foo == True:
    pass
```

- Correct code
```python
foo = True
if foo:
    pass
```

[^1]: [singleton comparison](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0121.html)

- Using `is` and `not <expression> is` instead

```python
#~~~
assert is_valid("CS50") is True

assert not is_valid("CS05") is True
# or
assert is_valid("CS05") is False
#~~~
```


Resources:
- [Python `!=` operation vs `is not`](https://stackoverflow.com/a/2209781/13041067)
