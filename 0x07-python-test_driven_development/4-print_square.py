#!/usr/bin/python3
"""print a square"""


def print_square(size):
    """print a square with the given size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
    if size == 0:
        print()
