#!/usr/bin/python3
def magic_string():
    """prints magic string"""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.n - 1)
