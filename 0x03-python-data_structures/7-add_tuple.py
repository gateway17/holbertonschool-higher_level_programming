#!/usr/bin/python3
# Write a function that adds 2 tuples.

#    Prototype: def add_tuple(tuple_a=(), tuple_b=()):
#    Returns a tuple with 2 integers:
#        The first element should be the addition of
# the first element of each argument.
#        The second element should be the addition of
# the second element of each argument.
#    You are not allowed to import any module
#    You can assume that the two tuples will only contain integers
#    If a tuple is smaller than 2, use the value 0 for each missing integer
#    If a tuple is bigger than 2, use only the first 2 integers


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = []
    if len(tuple_a) < 2:
        while len(tuple_a) < 2:
            tuple_a.append(0)
    elif len(tuple_b) < 2:
        while len(tuple_b) < 2:
            tuple_b.append(0)
    tuple_c.append(tuple_a[0] + tuple_b[0])
    tuple_c.append(tuple_a[1] + tuple_b[1])
    return tuple_c
