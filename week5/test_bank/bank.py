def main() -> int:
    """Main function"""
    greeting = input("Greeting: ")
    print("$", value(greeting), sep="")
    return 0


def value(greeting: str) -> int:
    """Evaluates the value of the greeting"""
    greeting = greeting.lower()
    if not greeting.startswith("h"):
        return 100
    if greeting.startswith("hello"):
        return 0
    return 20


if __name__ == "__main__":
    main()
    return 0
