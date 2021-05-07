#!/usr/bin/python3

# Write a function that returns a new
# dictionary with all values multiplied by 2.

#    Prototype: def multiply_by_2(a_dictionary):
#    You can assume that all values are only integers
#    Returns a new dictionary
#    You are not allowed to import any module


def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary
