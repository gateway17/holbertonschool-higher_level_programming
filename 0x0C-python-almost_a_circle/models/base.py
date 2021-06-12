#!/usr/bin/python3

class Base:
    """Creates "IDs" for instances. """

    __nb_objects = 0

    def __init__(self, id=None):
        """Creates an instance of Base """
        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
