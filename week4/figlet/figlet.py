"""
------
Figlet
------

Prompts the user for a string of text and Outputs that text either in a random
font or in the desired font.

Usage: python figlet.py [-f|--font FONT]

Source: https://cs50.harvard.edu/python/2022/psets/4/figlet/
"""

import random
import sys
from pyfiglet import Figlet


def main() -> int:
    """Main Function"""

    figlet: Figlet = Figlet()

    fonts: list[str] = figlet.getFonts()

    # Randomly choose a font
    if len(sys.argv) == 1:
        fnt: str = random.choice(fonts)
        figlet.setFont(font=fnt)
        output_text: str = figlet.renderText(input("Input: "))
    # Using the font provided at commandline (-f/--font FONT)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        fnt: str = sys.argv[2].strip()
        if fnt not in fonts:
            sys.exit("Invalid Font.")
        figlet.setFont(font=fnt)
        output_text: str = figlet.renderText(input("Input: "))
    else:
        sys.exit("usage: figlet [-f|--font FONT]")

    print("Output:\n", output_text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# pyright: reportMissingTypeStubs=false, reportUnknownMemberType=false
