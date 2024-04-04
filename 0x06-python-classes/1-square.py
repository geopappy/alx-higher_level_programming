#!/usr/bin/python3
""" creates a Square class """


class Square:
    """
    A class representing a square shape

    Attribues:
        __size (int): The size of the square
    """
    def __init__(self, size):
        """
        Initialize the square with the given size

        Parameter:
            size (int): The size of the square
        """

        self.__size = size
