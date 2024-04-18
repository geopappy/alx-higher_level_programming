#!/usr/bin/python3
"""0-read_file.py module"""


def read_file(filename=""):
    """
    Reads a file and prints its data.
    Args:
        filename: The file to be read.
    Returns:
        Nothing.
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
