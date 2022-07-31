"""
-------------------
Response Validation
-------------------

Validates input email using a validator library

Source: https://cs50.harvard.edu/python/2022/psets/7/response/
"""


# pyright: reportMissingTypeStubs=false
from validator_collection import checkers, errors


def main() -> int:
    """Main function"""
    print(validate(input("What's your email address? ")))
    return 0


def validate(email: str) -> str:
    """Validates an input email address"""
    try:
        email = validators.email(email)
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    raise SystemExit(main())
