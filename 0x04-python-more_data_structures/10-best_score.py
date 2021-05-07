#!/usr/bin/python3

# Write a function that returns a key with the biggest integer value.

#    Prototype: def best_score(a_dictionary):
#    You can assume that all values are only integers
#    If no score found, return None
#    You can assume all students have a different score
#    You are not allowed to import any module


def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    score = int(0)
    for i in a_dictionary:
        if a_dictionary[i] > score:
            score = a_dictionary[i]
            user = i
        else:
            continue
    return(user)


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
