#!/usr/bin/python3
def magic_calculation(a, b):
    print ("
            0 LOAD_CONST               1 (98)
            3 LOAD_FAST                0 (a)
            6 LOAD_FAST                1 (b)
            9 BINARY_POWER
            10 BINARY_ADD
            11 RETURN_VALUE

    ")

magic_calculation(0,2)