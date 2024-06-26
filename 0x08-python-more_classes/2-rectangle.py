#!/usr/bin/python3
"""This modulus contain the Rectangle class"""


class Rectangle:
    """
    A class representing a Rectangle shape

    Attribues:
        __width (int): The width of the rectangle
        __height (int): The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with the given width and height

        Parameter:
            width (int, optional): The width of the rectangle. Default to 0
            height (int, optional): The height of the rectangle. Default to 0

            Raises:
                TypeError: If width is not an integer or height is not an
                integer
                ValueError: If the width is less than 0 or height is less than
                0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of a rectangle

        Parameters:
            value (int): width of the rectangle

            Raises:
                TypeError: If width is not an integer
                ValueError: If the width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of a rectangle

        Parameters:
            value (int): height of the rectangle

            Raises:
                TypeError: If height is not an integer
                ValueError: If the height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of a rectangle.

        Returns:
            int: The area of a rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle.

        Returns:
            int: The perimeter of a rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return ((2 * self.__width) + (2 * self.__height))
