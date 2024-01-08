#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_even = []
    for n in my_list:
        is_even.append(n % 2 == 0)
    return is_even
