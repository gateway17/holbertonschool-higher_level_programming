#!/usr/bin/python3

"""
Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

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
    Public class attribute number_of_instances:
        Initialized to 0
        Incremented during each new instance instantiation
        Decremented during each instance deletion
    Public class attribute print_symbol:
        Initialized to #
        Used as symbol for string representation
        Can be any type
    Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self):
        that returns the rectangle perimeter:
        if width or height is equal to 0, perimeter has to be equal to 0
    print() and str() should print the rectangle with the character #:
        if width or height is equal to 0, return an empty string
    repr() should return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
    Print the message Bye rectangle... (... being 3 dots not ellipsis) when
        an instance of Rectangle is deleted
    Static method def bigger_or_equal(rect_1, rect_2):
        that returns the biggest rectangle based on the area
        rect_1 must be an instance of Rectangle, otherwise
            raise a TypeError exception with the message
            "rect_1 must be an instance of Rectangle"
        rect_2 must be an instance of Rectangle, otherwise
            raise a TypeError exception with the message
            "rect_2 must be an instance of Rectangle"
        Returns rect_1 if both have the same area value
    Class method def square(cls, size=0): that returns a new Rectangle instance
        with width == height == size
    You are not allowed to import any module
"""


class Rectangle:
    """docstring for ClassName"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize sizes for Triangle. """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

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
                string += str(self.print_symbol)
            string += "\n"
        string = string[:-1]
        return string

    def __del__(self):
        """Delates an Instance. """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares which rectangle is bigger. """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        else:
            rect_1.area_rect_1 = Rectangle.area(rect_1)
            rect_2.area_rect_2 = Rectangle.area(rect_2)

            if rect_1.area_rect_1 > rect_2.area_rect_2:
                return rect_1
            elif rect_2.area_rect_2 > rect_1.area_rect_1:
                return rect_2
            elif rect_1.area_rect_1 == rect_2.area_rect_2:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance. """
        new_R = cls(size, size)
        return new_R
