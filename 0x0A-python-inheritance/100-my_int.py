#!/usr/bin/python3
""" Defines class Myint"""


class MyInt(int):
    """class that reverses the equal and not equal to"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
