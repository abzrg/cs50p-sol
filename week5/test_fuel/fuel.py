"""
----------
Fuel Gauge
----------

Tells you how much fuel you have left with.

Source: https://cs50.harvard.edu/python/2022/psets/3/fuel/
"""


def main() -> int:
    """Main Function"""
    stat: str = ""
    while True:
        fraction: str = input("Fraction: ")
        if "/" not in fraction:
            continue

        try:
            stat = gauge(convert(fraction))
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(stat)

    return 0


def convert(fraction: str) -> int:
    """
    Converts a string fraction into (rounded) percentage
    """
    expr: list[str] = fraction.split("/", 1)
    numerator: int = int(expr[0])
    denominator: int = int(expr[1])

    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError

    return round(numerator / denominator * 100)


def gauge(percentage: int) -> str:
    """
    Common sense representation fo fuel capcity of a car
    """
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    raise SystemExit(main())
