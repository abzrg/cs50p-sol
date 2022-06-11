# Slows down the users text, with ellipses...!

# References:
#   1. https://docs.python.org/3/library/stdtypes.html#str.replace
#   2. https://docs.python.org/3/library/stdtypes.html#str.expandtabs


def main():
    print("Slower:", slow(input("Text: ")))


# Replaces all occurrences of spaces with ...
def slow(str: str, tabsize=4) -> str:
    # If there is a tab, convert it to (4) spaces
    return str.expandtabs(tabsize=tabsize).replace(" ", "...")


main()
