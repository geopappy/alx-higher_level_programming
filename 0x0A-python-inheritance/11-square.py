#!/usr/bin/python3

"""import Rectangle class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        prints a str rep for the rec.
        Returns:
            A string rep.
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"
