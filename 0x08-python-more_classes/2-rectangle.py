#!/usr/bin/python3

"""Set a Rectangle. """


class Rectangle:
    """Create a rectangle"""

    def __init__(self, width=0, height=0):
        """ Width and height values initialized"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns are of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter for rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
