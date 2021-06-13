#!/usr/bin/python3

from rectangle import Rectangle
"""
Sets and manage an Square
"""

class Square(Rectangle):
    """
    Methods.
    __init__ : Inicialize instances
    
    Magic methods.
    __str__ : Print values of right before mentioned\
    properties"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize values for Square
        arguments: size, x=0, y=0, id=None
        """
    
        #Calls to the super class
        super().__init__(size, size, x, y, id)


    @property
    def size (self):
        return self.width

    @size.setter
    def size (self, value):
        """Size setter. """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value


    def __str__(self):
        """ Print the data of properties."""
        form = "[Square] ({}) {}/{} - {}"
        return form.format\
            (self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):

        if args and args is not None:
            atritibuttes = ["id", "size", "x", "y"]

            for i in range(len(args)):         # Here goes an unittest
                if hasattr(self, atritibuttes[i]):    # What if they pass more than 4 parameter?
                    setattr(self, atritibuttes[i], args[i])
                    break

        else:
            if kwargs and kwargs is not None:

                for key, value in kwargs.items(): # Here goes a unittest
                    if hasattr(self, key):        # What if the properties they are refering
                        setattr(self, key, value)   # Doesn't exist?
                        break
