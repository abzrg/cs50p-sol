"""
------------
Coke Machine
------------

The machine accepts only the following denominations
-  5 cents
- 10 cents
- 25 cents

Source: https://cs50.harvard.edu/python/2022/psets/2/coke/
"""


def main() -> int:
    """Main function"""
    total: int = 0
    price: int = 50
    while True:
        amount_due: int = price - total

        if total >= price:
            break

        # Inform the user of the amount due
        print(f"Amount Due: {amount_due}")

        # Prompt the user to insert coin
        coin: int = int(input("Insert Coin: "))

        # Validate money, and add up
        denoms: list[int] = [5, 10, 25]
        denom: int
        for denom in denoms:
            if coin == denom:
                total += coin
                break

    # Inform the user of the change they owe
    print(f"Change Owed: {-1 * amount_due}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
