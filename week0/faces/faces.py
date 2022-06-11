def main():
    str = input("Text: ")
    print("Converted:", convert(str))


def convert(str: str) -> str:
    """
    Converts bunch of emoticons into equivalent emojis
    """
    str = str.replace(":)", "🙂")
    return str.replace(":(", "🙁")


main()
