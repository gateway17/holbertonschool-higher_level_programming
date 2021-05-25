#!/usr/bin/python3

"""
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

    Private instance attribute: width:
        property def width(self): to retrieve it
        property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError exception
            with the message width must be an integer
            if width is less than 0, raise a ValueError exception
            with the message width must be >= 0
    Private instance attribute: height:
        property def height(self): to retrieve it
        property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a TypeError exception
            with the message height must be an integer
            if height is less than 0, raise a ValueError exception
            with the message height must be >= 0
    Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self):
        that returns the rectangle perimeter:
        if width or height is equal to 0, perimeter has to be equal to 0
    print() and str() should print the rectangle with the character #:
        if width or height is equal to 0, return an empty string
    You are not allowed to import any module

"""


class Rectangle:
    """docstring for ClassName"""

    def __init__(self, width=0, height=0):
        """Initialize sizes for Triangle. """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns Triangle's width. """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets Rectangle's width  """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Returns Triangle's Height. """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets Rectangle's height (Setter)"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns area of Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints area of rectangle with '#' Character."""
        string = ''

        if self.__height == 0 or self.__width == 0:
            return ''

        for i in range(self.__height):
            for e in range(self.__width):
                string += '#'
            string += "\n"
        string = string[:-1]
        return string
