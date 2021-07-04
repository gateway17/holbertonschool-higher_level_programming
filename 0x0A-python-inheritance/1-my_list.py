#!/usr/bin/python3

"""
Write a class MyList that inherits from list:

    Public instance method: def print_sorted(self): that prints the list,
    but sorted (ascending sort)
    You can assume that all the elements of the list will be of type int
    You are not allowed to import any module
"""


class MyList(list):
    """inherits from list """
    def print_sorted(self):
        """Print sorted list. """
        print(sorted(list))



my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)