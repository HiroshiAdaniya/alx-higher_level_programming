#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total_sum = 0
    prev_value = 0

    if roman_string is None or not roman_string:
        return 0
    for i in reversed(roman_string):
        index = roman_dictionary[i]
        if index < prev_value:
            total_sum -= index
        else:
            total_sum += index
        prev_value = index
    return total_sum
