#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    remove_item = []
    for i in set_1:
        for j in set_2:
            if i == j:
                remove_item.append(i)
    for i in remove_item:
        set_1.remove(i)
        set_2.remove(i)
    new_list = set_1
    new_list.update(set_2)
    return new_list
