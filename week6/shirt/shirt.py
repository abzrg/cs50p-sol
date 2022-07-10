"""\
------------
CS50 P-Shirt
------------


Source: https://cs50.harvard.edu/python/2022/psets/6/shirt/
"""

import os
import sys
from PIL import Image, ImageOps


def main() -> int:
    """Main Function"""

    # Check command-line arguments
    argc: int = len(sys.argv)
    argc_expected: int = 3

    if argc < argc_expected:
        sys.exit("Too few command-line arguments")

    if argc > argc_expected:
        sys.exit("Too many command-line arguments")

    # Get file names from command-line
    fn_before: str = sys.argv[1]
    fn_after: str = sys.argv[2]

    # Check if extensions are either jpg, or png
    valid_mime_types: tuple[str, str] = (".jpg", ".png")

    if not fn_before.endswith(valid_mime_types):
        sys.exit("Invalid input")

    if not fn_after.endswith(valid_mime_types):
        sys.exit("Invalid output")

    # Check two files are of the same mime type
    _, fn_before_ext = os.path.splitext(fn_before)
    _, fn_after_ext = os.path.splitext(fn_after)
    if not fn_before_ext == fn_after_ext:
        sys.exit("Input and output have the different extensions")

    # Open inputs
    fn_shirt: str = "shirt.png"

    try:
        before = Image.open(fn_before)
        shirt = Image.open(fn_shirt)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    size: tuple[int, int] = shirt.size

    # Resize and crop
    before = ImageOps.fit(before, size)

    # Overlay shirt on image
    # src (mask=shirt): https://stackoverflow.com/a/5324782/13041067
    before.paste(shirt, mask=shirt)

    # Save into the after
    before.save(fn_after)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
