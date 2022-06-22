"""
----------
Fuel Gauge
----------

Tells you how much fuel you have left with.

Source: https://cs50.harvard.edu/python/2022/psets/3/fuel/
"""


def main() -> int:
    """Main Function"""
    capacity = get_capacity("Fraction: ")

    if capacity <= 1:
        print("E")
    elif capacity >= 99:
        print("F")
    else:
        print(f"{capacity}%")

    return 0


def get_capacity(prompt: str) -> float:
    """Gets the capacity in percentage"""
    while True:
        text: str = input(prompt)

        # Check if there is / in input
        if "/" not in text:
            continue

        # Split fraction (split at most once)
        fraction: list[str] = text.split("/", 1)

        try:
            numerator: int = int(fraction[0])
            denominator: int = int(fraction[1])

            # If numerator is greater than denominator, reprompt
            if numerator <= denominator:
                return round(numerator / denominator * 100)
        except (ZeroDivisionError, ValueError):
            pass



if __name__ == "__main__":
    raise SystemExit(main())
