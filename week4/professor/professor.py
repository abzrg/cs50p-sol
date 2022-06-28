"""
----------------
Little Professor
----------------

Prompts the user to solve each of those problem. If an answer is not correct (or
not even a number), the program should output EEE and prompt the user again,
allowing the user up to three tries in total. If the user has still not answered
correctly after three tries, the program should output the correct answer.

Source: https://cs50.harvard.edu/python/2022/psets/4/professor/
"""

import random


def main() -> int:
    """Main Function"""

    # Get level from user
    level: int = get_level()

    score: int = 0

    # Generate 10 random math problem
    for _ in range(10):
        # Produce two random operand
        lhs: int = generate_integer(level)
        rhs: int = generate_integer(level)

        # Get answer from user
        num_of_tries: int = 0
        while True:
            expression: str = f"{lhs} + {rhs} = "

            # Get answer from user
            try:
                num_of_tries += 1
                answer: int = int(input(expression))
            except ValueError:
                continue

            # Check if answer is correct
            if answer == lhs + rhs:
                score += 1
                break

            # If user has tried too many times, output the correct answer
            if num_of_tries == 3:
                print(expression + str(lhs + rhs))
                break

            # At this point the answer was wrong, so we should prompt the user
            # again
            print("EEE")

    print(f"score: {score}")
    return 0


def get_level() -> int:
    """Get level from user"""
    while True:
        try:
            level: int = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level: int) -> int:
    """Generate a random integer with level digits"""
    if level not in [1, 2, 3]:
        raise ValueError

    if level == 1:
        return random.randint(0, 9)

    return random.randint(10 ** (level - 1), 10**level - 1)


if __name__ == "__main__":
    raise SystemExit(main())
