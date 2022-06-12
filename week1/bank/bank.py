# $0  : hello, hello there, ...
# $20 : hey, hey there, ...
# $100: not starting with h

# Resources: https://docs.python.org/3.10/library/stdtypes.html#str.startswith


def main():
    # Prompt the user for greeting
    greeting = input("Greeting: ").lstrip().lower()

    # Evaluate the user's input
    print("$", greet_eval(greeting), sep='')


def greet_eval(str) -> int:
    if str.startswith('h'):
        if str.startswith("hello"):
            return 0
        return 20
    else:
        return 100


main()
