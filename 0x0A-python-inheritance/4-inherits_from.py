#!/usr/bin/python3
"""check instance of class"""


def inherits_from(obj, a_class):
    """check if the object is an instance
    of a class derived from the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
