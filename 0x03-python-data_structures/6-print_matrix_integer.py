#!/usr/bin/python3
# Write a function that prints a matrix of integers.

#   Prototype: def print_matrix_integer(matrix=[[]]):
#    Format: see example
#    You are not allowed to import any module
#    You can assume that the list only contains integers
#    You are not allowed to cast integers into strings
#    You have to use str.format() to print integers


def print_matrix_integer(matrix=[[]]):
    ctr1 = 0
    ctr2 = 0
    while ctr1 < len(matrix):
        while ctr2 < len(matrix[ctr1]):
            if ctr2 == (len(matrix[ctr1]) - 1):
                print("{:d}".format(matrix[ctr1][ctr2]))
            else:
                print("{:d} ".format(matrix[ctr1][ctr2]), end="")
            ctr2 += 1
        ctr2 = 0
        ctr1 += 1
