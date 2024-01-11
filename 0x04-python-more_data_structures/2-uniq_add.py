#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    return sum(set(my_list)) if len(my_list) else 0
