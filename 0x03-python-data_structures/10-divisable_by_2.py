#!/usr/bin/python3
def divisable_by_2(my_list=[]):
    is_even = []
    for i, n in enumerate(my_list):
        is_even[i] = n % 2 == 0
    return is_even
