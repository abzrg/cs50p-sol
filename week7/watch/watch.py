"""\
----------------
Watch on YouTube
----------------

Extract and shortens embedded YouTube URLs, per below:

  from:
      <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
  to:
      https://youtu.be/xvFZjo5PgG0

Source: https://cs50.harvard.edu/python/2022/psets/7/watch/
"""

import re


def main() -> int:
    """Main Function"""

    print(parse(input("HTML: ")))
    return 0


def parse(s: str) -> str:
    """\
    Parses an HTML element, iframe, and extract any YouTube URLs in 'src'
    attribute and shortens it.

    Assumptions:
      - Value of 'src' attribute will be in double quote.
      - Input contains no more than one URL.

    Return Value:
      - 'None', if the input does not contain any URL.
      - Shortened version of YouTube URL.
    """

    # (.+?): In between double quotes, perform non-greedy match
    if matches := re.search(
        r"^<.*src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/(.+?)\".*>$", s
    ):
        return "https://youtu.be/" + matches.group(1)

    return None


if __name__ == "__main__":
    raise SystemExit(main())
