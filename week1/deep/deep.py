# Let the user know if they know the "meaning of life, universe and
# everything"!


def main():
    # Prompt user for meaning of life
    mof = input("Meaning of Life: ").lower().strip()

    # Respond to user's answer
    if mof == "42" or mof == "forty-two" or mof == "forty two":
        print("Yes")
    else:
        print("No")


main()
