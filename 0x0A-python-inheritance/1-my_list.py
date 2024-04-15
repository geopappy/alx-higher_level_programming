#!/usr/bin/python3
"""Class mylist that inherits from list"""


class MyList(list):
    """Initializing the class
    def __init__(self):
        pass
"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
