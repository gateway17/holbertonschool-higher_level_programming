#!/usr/bin/python3

import json
"""
Write a function that returns the JSON representation of an object (string):

    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.

"""


def to_json_string(my_obj):
    """Creates json object by recived data. """
    x = json.dumps(my_obj)
    return x
