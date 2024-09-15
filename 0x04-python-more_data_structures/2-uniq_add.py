#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    total_sum = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            total_sum += i
    return total_sum
