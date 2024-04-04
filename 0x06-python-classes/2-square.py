#!/usr/bin/python3
""" creates a Square class """


class Square:
    """
    A class representing a square shape

    Attribues:
        __size (int): The size of the square
    """
    def __init__(self, size=0):
        """
        Initialize the square with the given size

        Parameter:
            size (int, optional): The size of the square. Default to 0

            Raises:
                TypeError: If size is not an integer.
                ValueError: If the size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >=0")

        self.__size = size
