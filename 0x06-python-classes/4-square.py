#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 3-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
    that returns the current square area
    You are not allowed to import any module
"""


class Square:
    """ Set a Square."""
    def __init__(self, size=0):
        """Set a Square"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        """Get the Square of the variable size """
        return self.__size

    @size.setter
    def size(self, value):
        """Set value for Square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns the the Square."""
        return self.__size ** 2
