"""\
-------
NUMB3RS
-------

Checks if an IPV4 address is valid or not

Source: https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
"""

import re


def main() -> int:
    """Main Function"""
    print(validate(input("IPv4 Address: ")))
    return 0


def validate(ip: str) -> bool:
    """\
    Checks if an IP address is a valid IPV4 address
    """

    # Use of "implicit string concatenation" technique to break down regex
    # pattern in to multiple lines
    matches = re.search(
        (  # Multi-line statement in between pair of parenthesis
            r"^"
            r"(?:"
            r"\d\d?|"  # One- and two-digit numbers
            r"1\d\d|"  # Three-digit numbers that start with 1 as hundreds
            r"2[0-4]\d|"  # Three-digit numbers in range [200, 249]
            r"25[0-5]"  # Three-digit numbers in range [250, 255]
            r")"
            r"\."
            r"(?:\d\d?|1\d\d|2[0-4]\d|25[0-5])"
            r"\."
            r"(?:\d\d?|1\d\d|2[0-4]\d|25[0-5])"
            r"\."
            r"(?:\d\d?|1\d\d|2[0-4]\d|25[0-5])"
            r"$"
        ),
        ip,
    )

    if not matches:
        return False
    else:
        return True


if __name__ == "__main__":
    raise SystemExit(main())
