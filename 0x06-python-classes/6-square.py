#!/usr/bin/python3
""" creates a Square class """


class Square:
    """
    A class representing a square shape

    Attribues:
        __size (int): The size of the square
        __position(tuple): The position of the square

    Mathod:
        area(): Calculate the area of a squar
        my_print(): Print the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with the given size and position

        Parameter:
            size (int, optional): The size of the square. Default to 0
            position (tuple, optional): The position of the square. Default to
            (0, 0)

            Raises:
                TypeError: If size is not an integer or position is not a tuple
                of two positive integers.
                ValueError: If the size is less than 0.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculate the area of a square.

        Returns:
            int: The area of a square
        """

        return (self.__size ** 2)

    def my_print(self):
        """ print square"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.size):
                print(' ' * self.__position[0] + "#" * self.size)

    @property
    def size(self):
        """Get size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of a square.

        Parameters:
            size(int): size of the square

            Raises:
                TypeError: If size is not an integer
                ValueError: If the size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        """Get position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square

        Parameters:
            value (tuple): The position of the square

        Raises:
            TypeError: If value is not a tuple or doesn't contain two positive
            integers
        """

        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all([type(i) is int and i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
