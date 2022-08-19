"""\
---------------
Seasons of Love
---------------

Prompts the user for their date of birth in YYYY-MM-DD format and then prints
how old they are in minutes, rounded to the nearest integer, using English
words instead of numerals, without any and between words.

- For simplicity, that the user was born at midnight (i.e., 00:00:00) on that
  date.
- Assume that the current time is also midnight.

Source: https://cs50.harvard.edu/python/2022/psets/8/seasons/
"""

import sys
import re
from datetime import date
from inflect import engine


def main() -> int:
    """Main Function"""

    # Get (correct) birthday
    birthday_str: str = input("Date of Birth: ").strip()
    if not validate(birthday_str):
        sys.exit("Invalid date")
    year, month, day = map(int, birthday_str.split("-"))
    birthday: date = date(year, month, day)

    # Get today
    today: date = date.today()

    # Get minutes elapsed since birth
    minutes: int = (today - birthday).days * 24 * 60

    # Convert minutes to words
    p: engine = engine()
    minutes_words: str = p.number_to_words(minutes)
    minutes_words = minutes_words.replace('and ', '').capitalize()
    print(minutes_words, "minutes")

    return 0

def validate(d: str) -> bool:
    """Validates a date string"""
    matches = re.search(r"(\d{4})-(\d{2})-(\d{2})", d)
    if not matches:
        return False

    year, month, day = map(int, matches.groups())

    # Check is date is in range
    try:
        date(year, month, day)
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    raise SystemExit(main())
