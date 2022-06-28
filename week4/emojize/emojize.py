"""
-------
Emojize
-------

Prompts the user for a str in English and then outputs the "emojized" version
of that str, converting any codes (or aliases) therein to their corresponding
emoji.

Source:  https://cs50.harvard.edu/python/2022/psets/4/emojize/
"""

from emoji import emojize


def main() -> int:
    """Main Function"""
    inpt: str = input("Input").strip()
    print(emojize(inpt, language="alias"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
