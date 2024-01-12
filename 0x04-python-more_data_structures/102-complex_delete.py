#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = set()
    for k, v in a_dictionary.items():
        if v == value:
            keys.add(k)

    for k in keys:
        del a_dictionary[k]

    return a_dictionary
