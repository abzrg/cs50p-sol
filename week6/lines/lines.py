"""
-------------
Lines of Code
-------------

- Expects exactly one command-line arguments
    - The name or path of a Python file
- Outputs the number of lines of code in that file, excluding
    - Blank lines
    - Comment lines

Source: https://cs50.harvard.edu/python/2022/psets/6/lines/
"""

import sys


def main() -> int:
    """Main Function"""

    # Check if user has provided the file name/path
    argc: int = len(sys.argv)

    if argc < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif argc > 2:
        print("Too many command-line arguments")
        sys.exit(2)

    # Check if the extension of the file is .py
    if not sys.argv[1].endswith(".py"):
        print("Not a python file")
        sys.exit(3)

    # Check if the file actually exists
    try:
        with open(sys.argv[1]) as file:
            loc: int = 0

            for line in file:
                if is_loc(line):
                    loc += 1

            print(loc)

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(4)

    return 0


def is_loc(line: str) -> bool:
    """
    Determines if a line of code in a file is part of the code
    and not blank or comment
    """
    if line.lstrip().startswith("#") or line.lstrip() == "":
        return False
    return True


if __name__ == "__main__":
    raise SystemExit(main())
