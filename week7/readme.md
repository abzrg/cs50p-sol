# Regular Expressions

- Regular Expressions
- Case Sensitivity
- Cleaning Up User Input
- Extracting User Input


## Regular Expressions

- One good website to poke around: [regex101](https://regex.101.com)

- A regular expression (shortened as regex or regexp; sometimes
  referred to as rational expression) is a sequence of characters that
  specifies a search pattern in text. Usually such patterns are used
  by string-searching algorithms for "find" or "find and replace"
  operations on strings, or for input validation. Regular expression
  techniques are developed in theoretical computer science and formal
  language theory. -- wikipedia

- `re` library

  - [Documentation](https://docs.python.org/3/library/re.html)


- Raw string:
  - Python raw string is created by prefixing a string literal with
    `r` or `R`. Python raw string treats backslash (`\`) as a literal
    character. This is useful when we want to have a string that
    contains backslash and don’t want it to be treated as an escape
    character.
  - [python: raw (NOT REGEX) r'strings'](https://www.youtube.com/watch?v=RvoKwGekk1s)


### Syntax of regular expression pattern


- `search` function: Scan through string looking for a match to the
  patern, returning a Match object, or None if no match was found

  ```python
  re.search(pattern, string, flags=0)
  ```

  ```python
  import re

  email = input("What is your email? ").strip()

  if re.search("^[^@]+@[^@]+\.edu$", email):
      print("Valid")
  else:
      print("Invalid")
  ```


  | Character | Meaning                                                                           |
  |:----------|:----------------------------------------------------------------------------------|
  | `.`       | Any character except a newline                                                    |
  | `*`       | 0 or more repetition                                                              |
  | `+`       | 1 or more repetition                                                              |
  | `?`       | 0 or 1 repetition                                                                 |
  | `{m}`     | m repetition                                                                      |
  | `{m,n}`   | m-n repetition                                                                    |
  | `^`       | matches the start of the string                                                   |
  | `$`       | matches the end of the string or just before the newline at the end of the string |
  | `[]`      | set of characters                                                                 |
  | `[^]`     | complementing the set                                                             |
  | `\d`      | decimal digit                                                                     |
  | `\D`      | not a decimal digit (complement of \d)                                            |
  | `\s`      | whitespace characters                                                             |
  | `\S`      | not a whitespace character                                                        |
  | `\w`      | word character, as well as numbers and the underscore                             |
  | `\W`      | not a word character                                                              |
  | `A\|B`    | either A or B                                                                     |
  | `(...)`   | a group                                                                           |
  | `(?:...)` | non-caputuring version                                                            |


- Non-greedy:
  - `*?`, `+?`, `??`
    - The `*`, `+`, and `?` qualifiers are all greedy; they match as
      much text as possible. Sometimes this behaviour isn’t desired;
      if the `RE <.*` is matched against `<a> b <c>`, it will match
      the entire string, and not just `<a>`. Adding `?` after the
      qualifier makes it perform the match in non-greedy or minimal
      fashion; as few characters as possible will be matched. Using
      the `RE <.*?>` will match only `<a>`.

  - `{m,n}?`
    - Causes the resulting `RE` to match from `m` to `n` repetitions
      of the preceding `RE`, attempting to match as few repetitions as
      possible. This is the non-greedy version of the previous
      qualifier. For example, on the 6-character string `aaaaaa`,
      `a{3,5}` will match 5 `a` characters, while `a{3,5}`? will only
      match 3 characters.


## Case Sensitivity


- built-in flags for `re.search()`

  ```python
  re.IGNORECASE  # or re.I
  re.MULTILINE   # or re.M
  re.DOTALL      # or re.S
  ```

- If you need to use multiple flags, _OR_ (`|`) them

  ```python
  x = re.findall(pattern=r'CAT.+?END', string='Cat \n eND', flags=re.IGNORECASE | re.DOTALL)
  ```

- Note that you can also use f-string instead of a normal literal
  string for the pattern.


- The correct email pattern:

  ```
  ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
  ```

## Cleaning Up User Input

- You should never trust the user of your program to hand you the correctly
  formatted data. There are various ways to program defensively against those
  invalid inputs.

  ```python
  import re

  name = input("What's your name? ").strip()
  matches = re.search(r"^(.+), (.+)$", name)
  if matches:
      last, first = matches.groups()
      name = f"{first} {last}"
  print(f"hello, {name}")
  ```

  - `re.search` can return a set of matches that are extracted from the user’s
  input. If match contains any matches then it evaluates to `True`.


- We can request specific groups back using `matches.group`.

  ```python
  import re

  name = input("What's your name? ").strip()
  matches = re.search(r"^(.+), (.+)$", name)
  if matches:
      last = matches.group(1)
      first = matches.group(2)
      name = f"{first} {last}"
  print(f"hello, {name}")
  ```

- The walrus `:=` operator assigns a value from right to left and allows us to
  ask a boolean question at the same time.

  ```python
  import re

  name = input("What's your name? ").strip()
  if matches := re.search(r"^(.+), *(.+)$", name):
      name = matches.group(2) + " " + matches.group(1)
  print(f"hello, {name}")
  ```


## Extracting User Input

- After validating and cleaning user's input, we can extract some specific bits
  of information we wish for.

- `re.sub(pattern, repl, string, count=0, flags=0)`
  - This method allows us to substitute a pattern with something else.

  ```python
  import re

  url = input("URL: ").strip()

  username re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
  print(f"Username: {username}")
  ```

- Using `re.search` to capture the part we want.
  - According to Twitter's documentation a regex pattern for username could be:
  `[a-z0-9_]+`

  ```python
  import re

  url = input("URL: ").strip()

  if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
      print(f"Username:", matches.group(1))
  ```


## Summary

- Python's regex syntax
- Usefull functions in `re` module
  - re.search()
  - re.match()
  - re.fullmatch()
  - re.sub()
  - re.findall()
  - re.compile
- Walrus operator (`:=`)
- groups:
  - capturing
  - non-capturing
- regex flags:
  - `re.I` or `re.IGNORECASE`
  - ...

