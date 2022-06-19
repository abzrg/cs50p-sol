"""
---------
camelCase
---------

This program converts a camel case string to a snake case string.

Source: https://cs50.harvard.edu/python/2022/psets/2/camel/
"""


def main() -> int:
    """Main Function"""
    text = input("Variable: ")
    print(camel2snake(text))
    return 0


# # Procedural approach
# def camel2snake(text: str) -> str:
#     """Converts a camel case string to a snake case string"""
#     for c in text:
#         if c.isupper():
#             text = text.replace(c, "_" + c.lower())
#     return text


# Functional approach
def camel2snake(text: str) -> str:
    """Converts a camel case string to a snake case string"""
    return "".join(["_" + c.lower() if c.isupper() else c for c in text])


if __name__ == "__main__":
    main()
