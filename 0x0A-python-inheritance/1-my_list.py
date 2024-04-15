#!/usr/bin/python3
"""Class mylist that inherits from list"""


class MyList(list):
    """Initializing the class"""
    def __init__(self):
        pass

    def print_sorted(self):
        """Prints the soretd list"""

        list_copy = self[:]
        list_copy.sort()
        print(list_copy)
