#!/usr/bin/python3

"""
Write a function that divides 2 integers and prints the result.

    Prototype: def safe_print_division(a, b):
    You can assume that a and b are integers
    The result of the division should be printed in the finally: section
    The print statement should start with Inside result:
    and be followed by the result
    You have to use "{}".format() to print the result
    Returns the value of the division, otherwise: None
    You have to use try: / except: / finally:
    You are not allowed to import any module
"""


def safe_print_division(a, b):

        value = None

        try:
                value = a / b
        except ZeroDivisionError:
                pass
        finally:
                print("Inside result: {}".format(value)
                return value
