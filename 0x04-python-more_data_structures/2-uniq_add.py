#!/usr/bin/python3
# Write a function that adds all unique integers in a list
# (only once for each integer).

#    Prototype: def uniq_add(my_list=[]):
#    You are not allowed to import any module


def uniq_add(my_list=[]):
    new_list = []
    suma = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for e in new_list:
        suma = suma + e
    return suma
