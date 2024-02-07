#!/usr/bin/python3
"""read a file"""


def read_file(filename=""):
    """read a file and print it"""
    with open(filename) as f:
        print(''.join(f.readlines()), end="")
