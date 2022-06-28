"""
-------------------
Bitcoin Price Index
-------------------

Source: https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
"""

import sys

import requests


def main() -> int:
    """Main Function"""

    # Get number of bitcoin from user (commandline)
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin: float = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Send request and recieve response
    usd: float = 0.0
    try:
        response: requests.models.Response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        )
        usd: float = bitcoin * float(response.json()["bpi"]["USD"]["rate_float"])
    except requests.exceptions.JSONDecodeError:
        sys.exit("JSON data could not be decoded")
    except requests.RequestException:
        sys.exit("Request failed")
    except ValueError:
        sys.exit("API response is not a number")

    print(f"${usd:,.4f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
