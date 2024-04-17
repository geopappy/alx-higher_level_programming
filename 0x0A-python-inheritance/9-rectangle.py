#!/usr/bin/python3


"""inherits from baseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Istantiation
            Validates the following attributes:
                - width
                - height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of a rec.
        Returns:
            The area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints a str rep for the rec.
        Returns:
            A string rep.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
