#!/usr/bin/python3
# Write a function that removes all characters c and C from a string.

#    Prototype: def no_c(my_string):
#    The function should return the new string
#    You are not allowed to import any module
#    You are not allowed to use str.replace()


def no_c(my_string):
    ctr = 0
    new_string = ""
    while ctr < len(my_string):
        if my_string[ctr] == 'C' or my_string[ctr] == 'c':
            ctr += 1
        else:
            new_string += my_string[ctr]
            ctr += 1
    return new_string
