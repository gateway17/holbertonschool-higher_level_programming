#!/usr/bin/python3

"""
Rectangle class:
Creates and manage a Rectangle
"""

from models.base import Base
# Base = __import__("models.base", fromlist=[None]).Base


class Rectangle(Base):
    """ Creates and manage a Rectangle.
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        def area(self)
        display(self)
        update(self, *args, **kwargs)
        def to_dictionary(self)

    Magic Methods:
        __str__(self)

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Sets size for Rectangle
        Arguments: width, height,[x=0, y=0], id=None
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Getter for width.
        Get Rectangle's width information. """

        return self.__width

    @width.setter
    def width(self, s_width):
        """Setter for width.
        Set Rectangle's width size."""

        if not isinstance(s_width, int):
            raise TypeError("width must be an integer")
        elif s_width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = s_width

    @property
    def height(self):
        """Getter for height.
        Get Rectangle's height information."""

        return self.__height

    @height.setter
    def height(self, s_height):
        """Setter for height. """

        if not isinstance(s_height, int):
            raise TypeError("height must be an integer")
        elif s_height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = s_height

    @property
    def x(self):
        """Getter for x.
        Get Rectangle's x coordenate information."""

        return self.__x

    @x.setter
    def x(self, s_x):
        """Setter for x. """

        if not isinstance(s_x, int):
            raise TypeError("x must be an integer")
        elif s_x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = s_x

    @property
    def y(self):
        """Getter for y.
        Get Rectangle's y coordenate information."""

        return self.__y

    @y.setter
    def y(self, s_y):
        """Setter for y. """

        if not isinstance(s_y, int):
            raise TypeError("y must be an integer")
        elif s_y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = s_y

    def area(self):
        """ Returns the area value of the instance."""

        return self.__width * self.__height

    def display(self):
        """Print to stdout the graphic representation
        of the object taking x and y as reference
        to the position of the object in the screen
        """

        for i in range(self.height):
            for e in range(self.width):
                print('#', end='')
            print("")

    def update(self, *args, **kwargs):
        """ Updates new values for varibles:
        self.id, self.width, self.height,self.x ,self.y
        """

        if args is not None and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 5 and hasattr(self, attributes[idx]):
                    setattr(self, attributes[idx], value)

        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    def __str__(self):
        """Print the data of each instance."""

        self.ft = "[Rectangle] ({}) {}/{} - {}/{}"
        return self.ft.format(self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Returns a Diccionary values of:
            x, y, id, height, width """

        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
