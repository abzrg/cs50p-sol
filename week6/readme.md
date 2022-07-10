# File I/O


## Contents

- File I/O
- `open`
- `with`
- CSV
- Binary Files and `PIL`


## File I/O

- Once the program is ended, all information gathered from the user or generated
  by the program is lost unless we store it beforehand in a file.

- File I/O is the ability of a program to take a file as input or create a file
  as output.

- Python's documentation on
  [`sorted`](https://docs.python.org/3/library/functions.html#sorted)


## `open`


- Open file and return a corresponding file object. If the file cannot be
  opened, an `OSError` is raised

  ```python
  open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
  ```

- `file` is a
  [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
  giving the pathname (absolute or relative to the current working directory) of
  the file to be opened.

- `mode` is an optional string that specifies the mode in which the file is
  opened.
  - default: `'r'`

  | Character | Meaning                                                         |
  |:----------|:----------------------------------------------------------------|
  | `'r'`     | open for reading (default)                                      |
  | `'w'`     | open for writing, truncating the file first                     |
  | `'x'`     | open for exclusive creation, failing if the file already exists |
  | `'a'`     | open for writing, appending to the end of file if it exitst     |
  | `'b'`     | binary mode                                                     |
  | `'t'`     | text mode (default)                                             |
  | `'+'`     | open for updating (reading and writing)                         |


- Example code

  ```python
  name = input("What's your name? ")

  file = open("names.txt", "a")
  file.write(f"{name}\n")
  file.close()
  ```
  - `file.write(name)` writes the formatted string to the text file.
  - The line after that closes the file.


## `with`

- The `with` keyword allows you to automate the closing of a file.
- Example:

  ```python
  name = input("What's your name? ")
  with open("names.txt", "w") as file:
      f.write(f"{name}\n")
  ```

- Reading from a file:

  ```python
  with open("names.txt", "r") as file:
      lines = file.readlines(file)

  for line in lines:
      # strip new line at the end as print adds one automatically for us
      print(line.rstrip())
  ```

- We could simplify the code as follows:

  ```python
  with open("names.txt") as file:  # we can omit 'r' as it is the default
      for line in file:
          print("hello", line.strip())
  ```

- We can sort names in a list

  ```python
  names: list[str] = []

  with open("names.txt", "r") as file:
      for line in file:
          names.append(line.rstrip())

  for name in sorted(names):
      print("hello", name)
  ```

- Python's documentation on
  [`open`](https://docs.python.org/3/library/functions.html#open)



## CSV

- Stands for "comma separated values"

- `students.csv`:

  ```
  Hermoine,Gryffindor
  Harry,Gryffindor
  Ron,Gryffindor
  Draco,Slytherin
  ```

- Example code: print which students lives where

  ```python
  with open("students.csv") as file:
      for line in file:
          name, house = line.rstrip().split(",")
          print(f"{name} is in {house}")
  ```

- Let's sort the students in output by student's name. But how we can sort a
  list of dictionaries. Unlike `int`s and `float`s and other primitive data
  types, there is not a certain way to compare two dictionary. How we can tell
  Python to sort our list by the keys in each dictionary. For that the `sorted`
  function allows us to pass a function as argument to tell it how to compare
  two dictionaries. Basically this is to define on what "key" the list of
  student will be sorted.  This is done by using the `key`.


  ```python
  students: list[dict[str, str]] = []

  with open("students.csv") as file:
      for line in file:
          name, house = line.rstrip().split(",")
          student = {"name": name, "house": house}
          students.append(student)


  def get_name(student: dict[str, str]) -> str:
      return student["name"]


  for student in sorted(students, key=get_name):
      print(f"{student['name']} is in {student['house']}")
  ```


- We can further improve this code as we only using `get_name` function only
  once. This is done by using `lambda` functions aka anonymous functions.


  ```python
  students: list[dict[str, str]] = []

  with open("students.csv") as file:
      for line in file:
          name, house = line.rstrip().split(",")
          students.append({"name": name, "house": house})

  for student in sorted(studetns, key=lambda student: student['name']):
      print(f"{student['name']}, is in {student['house']}")
  ```

- "Hey Python, here is a function that has no name: Given a `student`, access
  their `name` and return that to the `key`"



## `csv` library

- This library simply parses csv files.


### `csv.reader`

- Changing our text file:

  ```
  Harry,"Number Four, Privet Drive"
  Ron,The Burrow
  Draco,Malfoy Manor
  ```


  ```python
  import csv

  students = []

  with open("students.csv") as file:
      reader = csv.reader(file)
      for row in reader:
          students.append({"name": row[0], "home": row[1]})

  for student in sorted(students, key=lambda student: student["name"]):
      print(f"{student['name']} is from {student['home']}")
  ```

- A `reader` works in a for loop, where each iteration the `reader` gives us
  another `row` from our CSV file. This `row` itself is a _list_, where each
  value in the list corresponds to an element in that row.


### `DictReader`

- Adding a header

  ```
  name,home
  Harry,"Number Four, Privet Drive"
  Ron,The Burrow
  Draco,Malfoy Manor
  ```


  ```python
  import csv

  students = []

  with open("students.csv") as file:
      reader = csv.DictReader(file)
      for row in reader:
          students.append({"name": row["name"], "home": row["home"]})

  for student in sorted(students, key=lambda student: student["name"]):
      print(f"{student['name']} is in {student['home']}")
  ```

- `DictReader`, which returns one _dictionary_ at a time.
- This is an example of _coding defensively_. As long as the person designing
  the CSV file has inputted the correct _header information_ on the first
  line, we can access that information using our program.



### Write to a CSV file

  ```python
  import csv

  name = input("What's your name? ")
  home = input("Where's your home? ")

  with open("students.csv", "a") as file:
      writer = csv.DictWriter(file, fieldnames=["name", "home"])
      writer.writerow({"name": name, "home": home})
  ```

- `DictWriter` takes two parameters: the `file` being written to and the
  `fieldnames` to write. Further, notice how the `writerow` function takes a
  dictionary as its parameter. Quite literally, we are telling the compiler to
  write a row with two fields called `name` and `home`


## Pillow

- A __binary__ file is simply a collection of ones and zeros. This type of file can
  store anything including, music and image data.

- Documentation for [PIL](https://pillow.readthedocs.io/)

  ```python
  import sys

  from PIL import Image

  images = []

  for arg in sys.argv[1:]:
      image = Image.open(arg)
      images.append(image)

  images[0].save(
      "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
  )
  ```

- Notice that we import the `Image` functionality from `PIL`. Notice that the
  first `for` loop simply loops through the images provided as command-line
  arguments and stores theme into the `list` called `images`. The `1:` starts
  slicing `argv` at its second element. The last lines of code saves the first
  image and also appends a second image to it as well, creating an animated
  gif. Run: `python costumes.py costume1.gif costume2.gif`
