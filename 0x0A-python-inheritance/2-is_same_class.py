#!/usr/bin/python3
"""check instance of class"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the specified class"""
    return type(obj) is a_class
