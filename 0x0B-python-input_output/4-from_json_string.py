#!/usr/bin/python3
"""import json"""
import json


def from_json_string(my_str):
    """Parse the JSON string and return
    the Python data structure
    Parameters:
        my_str: string to parse
    Returns:
        object
    """

    return json.loads(my_str)
