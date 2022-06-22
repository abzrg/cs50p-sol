"""
--------
Outdated
--------

Date format:
- US: MM/DD/YYYY
- ISO 8601: YYYY/MM/DD/

Input date format (AD):
- 9/8/1636
- September 8, 1636

Source: https://cs50.harvard.edu/python/2022/psets/3/outdated/
"""

months: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main() -> int:
    """Main Function"""

    while True:
        raw_date: str = input("Date: ").strip()

        # Dates with '/' in them
        if "/" in raw_date:
            date: list[str] = raw_date.split("/", 2)
            try:
                month: int = int(date[0])
                day: int = int(date[1])
                year: int = int(date[2])
                if is_date(day, month, year):
                    print(f"{year}-{month:02}-{day:02}")
                    break
            except ValueError:
                pass

        # Dates with ',' in them
        elif "," in raw_date:
            date: list[str] = raw_date.split(",")
            month_and_day: list[str] = date[0].split(" ")
            try:
                day: int = int(month_and_day[1])
                month: int = months.index(month_and_day[0]) + 1
                year: int = int(date[1])
                if is_date(day, month, year):
                    print(f"{year}-{month:02}-{day:02}")
                    break
            except ValueError:
                pass

    return 0


def is_date(day: int, month: int, year: int) -> bool:
    """Check if date is in range"""
    if day <= 31 and month <= 12 and year <= 9999 :
        return True
    return False


if __name__ == "__main__":
    raise SystemExit(main())
