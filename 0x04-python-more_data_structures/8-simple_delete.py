#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_diction = {}

    for i, j in a_dictionary.items():
        new_diction.update(dict([(i, j)]))

    for i, j in new_diction.items():
        if i == key:
            del a_dictionary[i]

    return a_dictionary
