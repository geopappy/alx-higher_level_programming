#!/usr/bin/python3
"""import json"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves a python dict to a json file.
    Args:
        my_obj: The obj to be converted and saved.
        filename: The file it should be saved to.
    Returns:
        Nothing.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
