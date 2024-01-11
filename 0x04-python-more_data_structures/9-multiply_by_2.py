#!/usr/bin/python3
def multiply_by_2(a_dictionary: dict):
    for k in a_dictionary:
        a_dictionary[k] *= 2
    return a_dictionary
