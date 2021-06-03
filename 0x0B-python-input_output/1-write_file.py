#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

    Prototype: def write_file(filename="", text=""):
    You must use the with statement
    You don’t need to manage file permission exceptions.
    Your function should create the file if doesn’t exist.
    Your function should overwrite the content of the file if it already exists.
    You are not allowed to import any module
"""


def write_file(filename="", text=""):

    with open(filename,'r+', encoding="UTF-8") as buffer:
        text = str(text)
        ctr = buffer.write(text)
    return ctr



nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
print(nb_characters)
