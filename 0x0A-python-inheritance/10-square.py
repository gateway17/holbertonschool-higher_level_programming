#!/usr/bin/python3

"""(inherits from Rectangle) """
Rectangle = __import__('9-rectangle').Rectangle


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
