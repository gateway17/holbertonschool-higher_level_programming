#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 5-square.py)

    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    size must be an integer, otherwise raise a TypeError exception
    with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
    position must be a tuple of 2 positive integers,
    otherwise raise a TypeError exception
    with the message position must be a tuple of 2 positive integers
    Instantiation with optional size and optional position:
        def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
    position should be use by using space
    - Don’t fill lines by spaces when position[1] > 0
    You are not allowed to import any module

"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter of __position
        Returns:
            The coordenates of the print position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): coordenates to print area
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates the area of the square.
        Returns:
            The area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square
        prints a graphic representation of the area with a '#'
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for hash in range(self.__position[0]):
                    print(" ", end="")
                for hash in range(self.__size):
                    print("#", end="")
                print()
