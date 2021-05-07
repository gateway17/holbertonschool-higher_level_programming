#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix.

#    Prototype: def square_matrix_simple(matrix=[]):
#    matrix is a 2 dimensional array
#    Returns a new matrix:
#        Same size as matrix
#        Each value should be the square of the value of the input
#    Initial matrix should not be modified
#    You are not allowed to import any module
#    You are allowed to use regular loops, map, etc.


def square_matrix_simple(matrix=[]):

    new_matrix = []
    for e in matrix:
        new_matrix.append([i**2 for i in e])

    return new_matrix
