#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return
    result = sum(set(my_list))
    result = result if result else 0
    return result
