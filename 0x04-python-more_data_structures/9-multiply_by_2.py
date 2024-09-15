#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_diction = {}

    for i, j in a_dictionary.items():
        new_diction.update(dict([(i, j * 2)]))
    return new_diction
