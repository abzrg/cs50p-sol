"""
------------
Grocery List
------------

Lists and counts the items provided by the user (one item per line) in
a grocery list.

Source: https://cs50.harvard.edu/python/2022/psets/3/grocery/
"""


def main() -> int:
    """Main Function"""
    groc_list: dict[str, int] = {}

    while True:
        try:
            item: str = input().strip()
            groc_list[item] = groc_list.get(item, 0) + 1
        except EOFError:
            print()
            break

    for item in sorted(groc_list):
        print(groc_list[item], item.upper())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
