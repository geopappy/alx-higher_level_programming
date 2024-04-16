#!/usr/bin/python
"""Documenting module"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of class which is a subclass of a class
    Arguments:
        obj (any): the object to be checked
        a_class (type): The class to match to
    Return:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
