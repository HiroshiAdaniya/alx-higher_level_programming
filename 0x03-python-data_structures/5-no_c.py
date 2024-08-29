#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    str_copy = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            str_copy = str_copy + c
    return str_copy
