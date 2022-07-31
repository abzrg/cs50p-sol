"""\
-----------------------
Regular, um, Expression
-----------------------

Counts the number of times that “um” appears in that text, case-insensitively,
as a word onto itself, not as a substring of some other word

- NOTE:
    - Case-insensitively
    - As a word onto itself

Source: https://cs50.harvard.edu/python/2022/psets/7/um/
"""

import re


def main() -> int:
    """Main Function"""
    print(count(input("Text: ")))
    return 0


def count(text: str) -> int:
    """Counts the number of occurence of um"""
    matches: list[str] = re.findall(r"\bum\b", text, flags=(re.IGNORECASE))
    if matches:
        return len(matches)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
