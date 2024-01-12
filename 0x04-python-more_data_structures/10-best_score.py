#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if a_dictionary is None:
        return
    mx = max(a_dictionary.items(), default=None, key=lambda x: x[1])
    return mx[0] if mx else mx
