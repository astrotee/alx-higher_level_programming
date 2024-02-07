#!/usr/bin/python3
"""write a file"""


def append_write(filename="", text=""):
    """append text to file"""
    with open(filename, 'a') as f:
        return f.write(text)
