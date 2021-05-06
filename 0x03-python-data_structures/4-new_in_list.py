#!/usr/bin/python3
# Write a function that replaces an element in a list at a specific position
# without modifying the original list (like in C).
#
#    Prototype: def new_in_list(my_list, idx, element):
#    If idx is negative, the function should return a copy of the original list
#    If idx is out of range (> of number of element in my_list),
#    the function should return a copy of the original list
#    You are not allowed to import any module
#    You are not allowed to use try/except


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element
    return new_list
