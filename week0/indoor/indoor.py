# WRITING IN ALL CAPS IS LIKE YELLING.


def main():
    # Prompt the user to enter a string, make it lowercase
    # and then print it
    print("Shush:", indoor(input("Text: ")))


# Makes the string lowercase
def indoor(voice: str) -> str:
    return voice.lower()


main()
