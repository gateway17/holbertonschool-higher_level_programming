#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
"""(inherits from Rectangle) """


class Square(Rectangle):
    """Sets a Square. """

    def __init__(self, size):
        """Initialize size for Square """
        self.integer_validator("Value", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of Square"""
        return self.__size**2

    def __str__(self):
        """Return values for Square """
        return "[Square] {}/{}".format(self.__size, self.__size)
