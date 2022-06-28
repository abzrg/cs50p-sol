"""
-------------
Guessing Game
-------------

Guess a number between 1 and the level.

Sources:
    - https://cs50.harvard.edu/python/2022/psets/4/game/
    - https://docs.python.org/3/library/random.html
"""

import random


def main() -> int:
    """Main Function"""

    # Get the level
    while True:
        try:
            level: int = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    # Set the value of the game
    value: int = random.randint(1, level)

    # Get the guess
    while True:
        try:
            guess: int = int(input("Guess: "))
            if guess < value:
                print("Too small!")
            elif guess > value:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
