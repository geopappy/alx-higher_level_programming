#!/usr/bin/python3
"""8-class_to_json.py module"""


def class_to_json(obj):
    """
    Turns a class atttibutes to json.
    Args:
        obj: object to return its class attribute
    Returns:
        dictionarg description of object class attributes
    """
    return obj.__dict__
