"""
-----------------
Felipe’s Taqueria
-----------------

Prompts user to enter an entree and give them price.
End the program using <C-d> signal from keyboard

Source: https://cs50.harvard.edu/python/2022/psets/3/taqueria/
"""

entrees: dict[str, float] = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main() -> int:
    """Main Function"""

    total: float = 0.0

    while True:
        try:
            item: str = input("Item: ").strip().title()
        except EOFError:
            print()  # New line after <C-d>
            break

        # Compute the total and print it
        total += entrees.get(item, 0)
        output: str = f"Total ${total:.2f}\n"
        print(output if item in entrees else "", end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
