"""
-------------
Vanity Plates
-------------

Validates plates against the following rules:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers)
  and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end.
  For example, AAA222 would be an acceptable … vanity plate; AAA22A would not
  be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”

Source: https://cs50.harvard.edu/python/2022/psets/2/plates/
"""


def main() -> int:
    """Main function"""
    plate: str = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    return 0


def is_valid(plate: str) -> bool:
    """
    Chack if the plate is valid accoring to the rules
    Assume that any letters in the user’s input will be uppercase
    """
    length = len(plate)

    if length < 2 or length > 6 or not plate[0:2].isalpha() or not plate.isalnum():
        return False

    # Find the index of the first numeric character
    index: int = 2
    char: str
    for char in plate[2:length]:
        if char.isnumeric():
            if char == "0":
                return False
            break
        index += 1

    # If after the first numeric character there are any alphanumeric characters
    # then it is invalid
    for char in plate[index:length]:
        if char.isalpha():
            return False

    # If you readched the end of the string and couldn't find the first number
    # then it is valid
    return True


if __name__ == "__main__":
    raise SystemExit(main())
