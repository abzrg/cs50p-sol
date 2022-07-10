"""\
---------
Scourgify
---------

Cleans a csv file, breaking a name into first and last name fields.

Source: https://cs50.harvard.edu/python/2022/psets/6/scourgify/
"""

import csv
import sys


def main() -> int:
    """Main Function"""

    # Get two command-line arguments
    argc: int = len(sys.argv)

    if argc > 3:
        sys.exit("Too many command-line arguments")

    if argc < 3:
        sys.exit("Too few command-line arguments")

    # Read original csv file
    before: str = sys.argv[1]
    students: list[dict[str, str]] = []
    try:
        with open(before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                student: dict[str] = row
                last, first = student["name"].replace(", ", ",").split(",")
                house: str = student["house"]
                students.append({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("")

    # Write changes into a new file
    after: str = sys.argv[2]
    with open(after, "w") as file:
        header: list[str] = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
