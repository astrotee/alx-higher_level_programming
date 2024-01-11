#!/usr/bin/python3
def only_diff_elements(set_1: set, set_2: set):
    if set_1 is None:
        return set_2
    elif set_2 is None:
        return set1
    return set_1.symmetric_difference(set_2)
