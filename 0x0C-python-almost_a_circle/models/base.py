#!/usr/bin/python3
"""
Base module
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionary into str
            returns string. """

        new_d = '"[]"'
        if list_dictionaries is None:
            return str(new_d)
        else:
            if type(list_dictionaries) is list:  # Unittest
                # list_dic is a list of dic, How do i know it is
                # really dicts? Make sure
                return json.dumps(list_dictionaries)
"""
    @classmethod
    def save_to_file(cls, list_objs):
        new = dict
# Unittest, What if the list of instances are from diferents classes?
        if not list_objs:
            return new
        else:
            # 1) Get list to str
            data = Base.to_json_string(list_objs)
            filename = str(cls.__name__ + ".json")
            # 2) Open file, in write mode
            with open(filename,'w', encoding="UTF-8") as buffer:

                json.dump(buffer, data)
"""
