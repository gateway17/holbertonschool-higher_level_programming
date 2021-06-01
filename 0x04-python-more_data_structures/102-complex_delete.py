#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    for i in a_dictionary:
        if a_dictionary[i] == value:
            pass
            a_dictionary.remove(i)

        print(a_dictionary)



a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
