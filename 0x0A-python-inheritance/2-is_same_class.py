#!/usr/bin/python3
""" Function tests if object is an instance of a class"""


def is_same_class(obj, a_class):
    """ define the function """
    if type(obj) is (a_class):
        return True
    else:
        return False
