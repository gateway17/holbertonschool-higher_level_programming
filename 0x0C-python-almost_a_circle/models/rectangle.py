#!/usr/bin/python3

from base import Base


class Rectangle(Base):
    """Creates a Rectangle. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Sets size for Rectangle
        Arguments: width, height,[x=0, y=0] """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y
        
        super().__init__(id)

    @property
    def width(self):
        """Getter for width. """
        return self.__width

    @width.setter
    def width(self, s_width):
        """Setter for width. """
        if not isinstance(s_width, int):
            raise TypeError("width must be an integer")
        elif s_width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = s_width

    @property
    def height(self):
        """Getter for height. """
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
        """Getter for x. """

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
        """Getter for y. """
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
        """ Prints the Rectangle in stdout."""
        for i in range(self.__height):
            for e in range(self.__width):
                print('#', end='')
            print("")

    def update(self, *args, **kwargs):
        """ Updates new values for varibles:
        self.id, self.__width, self.__height,self.__x ,self.__y
        """

        if args is not None and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for idx, value in enumerate(args):
                if idx < 5 and hasattr(self, attributes[idx]):
                    setattr(self, attributes[idx], value)

                else:
                    print("Aparentemente no tiene", attributes[idx])
            
        else:
            print("No entra al if")


    def __str__(self):
        """Print the data of each instance."""
        self.ft = "[Rectangle] ({}) {}/{} - {}/{}"
        return (self.ft.format(self.id, self.__x, self.__y, self.__width, self.__height))


r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)