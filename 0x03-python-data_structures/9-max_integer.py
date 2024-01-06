#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mx = my_list[0]
    for i in my_list:
        mx = i if i > mx else mx

    return mx
