"""
------------------------
Just setting up my twttr
------------------------

Shortens words to save time or space, as by omitting vowels, much like Twitter
was originally called twttr

Source: https://cs50.harvard.edu/python/2022/psets/2/twttr/
"""


def main() -> int:
    """Main function"""
    text: str = input("Input: ")
    print("Output:", shorten(text))
    return 0


def shorten(text: str) -> str:
    """Shortens text by removing vowels"""
    vowels: str = "aeiou"
    char: str
    for char in text:
        if char.lower() in vowels:
            text = text.replace(char, "")
    return text


if __name__ == "__main__":
    raise SystemExit(main())
