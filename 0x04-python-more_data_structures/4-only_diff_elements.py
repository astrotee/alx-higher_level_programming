#!/usr/bin/python3
def only_diff_elements(set_1: set, set_2: set):
    if None in (set_1, set_2):
        return set()
    return set_1.difference(set_2)
