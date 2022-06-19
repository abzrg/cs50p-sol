"""
---------------
Nutrition Facts
---------------

Gives the amount of calories for a fruit

Source: https://cs50.harvard.edu/python/2022/psets/2/nutrition/
"""

fruits: dict[str, int] = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}


def main() -> int:
    """Main function"""
    fruit: str = input("Item: ").strip().lower()
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
