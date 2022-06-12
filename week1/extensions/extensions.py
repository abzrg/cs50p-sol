# A program that prompts the user for the name of a file and then
# outputs that file's media type.

# Resources: https://docs.python.org/3.10/library/stdtypes.html#str.endswith


def main():
    # Ask the user for file name
    filename = input("File: ").strip()

    # Determine the MIME type
    print(mime_type(filename))


def mime_type(filename: str) -> str:
    fn_lower = filename.lower()

    if fn_lower.endswith(".gif"):
        return "image/gif"
    elif fn_lower.endswith((".jpg", ".jpeg")):
        return "image/jpeg"
    elif fn_lower.endswith(".png"):
        return "image/png"
    elif fn_lower.endswith(".pdf"):
        return "application/pdf"
    elif fn_lower.endswith(".txt"):
        return "text/plain"
    elif fn_lower.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()
