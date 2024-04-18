#!/usr/bin/python3
"""1-write_file.py module"""


def write_file(filename="", text=""):
    """
    write to a file.
    Args:
        filename: The file to write to.
        text: content to write
    Returns:
        number of character written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        char_no = f.write(text)
        print(char_no)
