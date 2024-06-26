#!/usr/bin/python3
"""1-write_file.py module"""


def append_write(filename="", text=""):
    """
    append to a file.
    Args:
        filename: The file to write to.
        text: content to write
    Returns:
        number of character written.
    """

    with open(filename, 'a', encoding="utf-8") as f:
        char_no = f.write(text)
        return len(text)
