#!/usr/bin/python3

"""import Json"""
import json


def to_json_string(my_obj):
    """
    Turn obj to json.
    Args:
        my_obj: The obj to be turned.
    Returns:
        JSON data
    """
    data = json.dumps(my_obj)
    return data
