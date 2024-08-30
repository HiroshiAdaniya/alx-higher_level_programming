#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    cpy_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            cpy_list[i] = True
        else:
            cpy_list[i] = False
    return cpy_list
