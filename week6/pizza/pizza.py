"""\
--------
Pizza Py
--------

Shows a Ascii table representation of a pizza menu (csv)

Source: https://cs50.harvard.edu/python/2022/psets/6/pizza/
"""

import csv
import sys
from tabulate import tabulate


def main() -> int:
    """Main Function"""

    # Check correct number of command-line arguments
    argc: int = len(sys.argv)

    if argc > 2:
        sys.exit("Too many command-line arguments")

    if argc < 2:
        sys.exit("Too few command-line arguments")

    # Check for file itself
    filename: str = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            rows: list[list[str]] = []
            for row in reader:
                rows.append(row)
            print(tabulate(rows[1:], rows[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
