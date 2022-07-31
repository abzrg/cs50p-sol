"""\
--------------
Working 9 to 5
--------------

Converts a range of 12-hour format time to a 24-hour one.

Source: https://cs50.harvard.edu/python/2022/psets/7/working/
"""

import re


def main() -> int:
    """Main Function"""
    print(convert(input("Hours: ")))
    return 0


def convert(time_range: str) -> str:
    """\
    converts a 12-hour format time range into 24-hour one.

    from:
        9:00 AM to 5:00 PM
        9 AM to 5 PM
    to:
        9:00 to 17:00
    """

    matches = re.search(
        r"^"
        r"("
        r"(?:\d|1[0-2])"  # Either match 0-9 or 10-12
        r"(?::[0-5]\d)?"  # Optionally ':' and a number in range 0-59
        r")"
        r" ([AP]M)"
        r" to "
        r"((?:\d|1[0-2]|\d|1[0-2])(?::[0-5]\d)?) ([AP]M)$",
        time_range,
    )

    if not matches:
        raise ValueError

    start: dict[str, str] = {"time": matches.group(1), "meridiem": matches.group(2)}
    end: dict[str, str] = {"time": matches.group(3), "meridiem": matches.group(4)}

    start_24_hour: str = time_12_to_24(start)
    end_24_hour: str = time_12_to_24(end)

    return f"{start_24_hour} to {end_24_hour}"


def time_12_to_24(time: dict[str, str]) -> str:
    """\
    Converts a 12-hour format time (with meridiem) to a 24-hour one.
    """
    time_24: str = ""

    if ":" in time["time"]:
        hour, minute = map(int, time["time"].split(":"))
        if time["meridiem"] == "AM":
            time_24 = (
                f"{(hour - 12):02}:{minute:02}"
                if hour == 12
                else f"{hour:02}:{minute:02}"
            )
        else:
            time_24 = (
                f"{hour:02}:{minute:02}"
                if hour == 12
                else f"{(hour + 12):02}:{minute:02}"
            )
    else:
        hour: int = int(time["time"])
        minute: int = 0
        if time["meridiem"] == "AM":
            if hour == 12:
                time_24 = f"{(hour - 12):02}:{minute:02}"
            else:
                time_24 = f"{hour:02}:{minute:02}"
        else:
            if hour == 12:
                time_24 = f"{hour:02}:{minute:02}"
            else:
                time_24 = f"{(hour + 12):02}:{minute:02}"

    return time_24


if __name__ == "__main__":
    raise SystemExit(main())
