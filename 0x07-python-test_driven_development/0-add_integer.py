#!/usr/bin/python3
"""define a function to add 2 ints"""


def add_integer(a, b=98):
    """ return the sum of ints a and b """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
