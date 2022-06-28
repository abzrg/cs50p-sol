# Library

## Keywords <!--  -->

- Library, Module (a library implemented in a python file), Package (a library
  implemented in a folder)
- Python's standard library
  - `random`
    - `choice([seq])`: return a random item from the sequence (list, dict, ...)
    - `randint(a: int, b: int)`: (Inclusive range)
    - `shuffle([seq])`: shuffles the list in place. (No return value)
  - statistics
    - `mean([seq])`: arithmetic average of data
  - `sys`
    - `sys.argv`: a variable. A list of command-line arguments (argument vector)
- `import` keyword


## Import <!--  -->

```python
# Import everything in random, without polluting namespace
import random

# Only import choice function from random and add to current file's namespace
from random import choice

# Import everything in random, and include them into the current file's
# namespace
from random import *
```

- If you are using `from` keyword, then you cannot do the following

```python
from random import choice

coin = random.choice(['heads', 'tails'])
print(coin)
```

### random (package)

- `choice(seq)` -- returns a random thing from within the seq
```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```

- `randint(a, b)` -- inclusive range
```python
import Random

number = random.randint(1, 10)
print(number)
```


- `shuffle(seq)` -- in place change (No return value)
```python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
      print(card)
```


### statistics (package)

```python
import statistics

print(statistics.mean([100, 90]))
```



## Command-line arguments <!--  -->

- with exceptions
```python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```


- with if statements
```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
```

### Slice

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```


## Packages <!--  -->

- A module implemented in a folder
- More generally a 3rd party library that we can install on our system

- [PyPI](https://pypi.org)
  - (Python Package Index): Location where you can get packages

### [cowsay](https://pypi.org/project/cowsay)

- pip: python's package manager
    ```bash
    pip install cowsay
    ```

```python
import cowsay
import sys

if len(sys.argv) == 2:
      cowsay.trex("hello, " + sys.argv[1])
```


## API (Application User interface) <!--  -->

- APIs or “application program interfaces” allow you to connect to the code of others.

### request (package)

- a package that allows your program to behave as a web browser would.
- `pip install requests`
- [documentation](https://docs.python-requests.org)
- `request.get(url: str) -> response`
- `response.json()`
- example:
  - "https://itunes.apple.com/search?entity=song&limit=1&term=weezer"
    - this query is looking for a song, with a limit of one result, that
      relates to the term called weezer.

```python
import requests
import system

if len(sys.argv) != 2
      sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term="
    + sys.argv[1])
print(response.json())
```

### json (package)

- One of the Python's built-in packages
- [documentation](https://docs.python.org/3/library/json.html)
- `dumps()`: pretty print (with indentation)

```python
import json
import requests
import system

if len(sys.argv) != 2
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))
```

```python
import json
import requests
import system

if len(sys.argv) != 2
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for results in o["results"]:
    print(result["trackName"])
```

## Making your own library

- `saying.py`: implement lib
```python
def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")
```

- say.py: use lib
```python
import sys

from saying import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
```

## [Glossary](https://docs.python.org/3/glossary.html)

- Package:
  - A Python module which can contain submodules, or recursively, subpackages.
  - Technically a package is a Python module with an `__path__` attribute.

- Module:
  - An object that serves as an organizational unit of Python code.
  - Modules have a namespace containing arbitrary Python objects.
  - Modules are loaded into Python by the process of importing.

  ```python
  from foo.bar.baz import great_function
  ```
    - foo: package
    - bar: subpackage
    - baz: submodule



## Resources

- [random](https://docs.python.org/3/library/random.html)
- [statistics](https://docs.python.org/3/library/statistics.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [Beautiful Soup]() package for web scraping
