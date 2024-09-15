#!/usr/bin/python3
def best_score(a_dictionary):
    highest_score = 0
    student = ""
    if a_dictionary is None:
        return None
    for i, j in a_dictionary.items():
        if j > highest_score:
            highest_score = j
            student = i
    return student
