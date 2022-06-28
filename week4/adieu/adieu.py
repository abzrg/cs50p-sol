"""
-----
Adieu
-----

Say goodbye (grammatically correct) to a list of names!

Sources:
    - https://cs50.harvard.edu/python/2022/psets/4/adieu/
    - https://pypi.org/project/inflect/
"""

import inflect


def main() -> int:
    """Main Function"""

    names: list[str] = []
    while True:
        try:
            name: str = str(input("Name: ")).strip()
            names.append(name)
        except EOFError:
            print("\n", end="")
            break

    grammar = inflect.engine()

    print("Adieu, adieu, to", grammar.join(names))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
