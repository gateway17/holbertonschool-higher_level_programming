#!/usr/bin/python3
# Write a function that returns a tuple with the length of a string
# and its first character.

#   Prototype: def multiple_returns(sentence):
#    If the sentence is empty, the first character should be equal to None
#    You are not allowed to import any module


def multiple_returns(sentence):
    new_tuple = ()
    if sentence:
        new_tuple = len(sentence), sentence[0]
    else:
        new_tuple = 0, None
    return new_tuple
