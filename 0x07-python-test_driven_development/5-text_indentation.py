#!/usr/bin/python3
"""print with indentation"""


def text_indentation(text: str):
    """print a square with the given size"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i, j = 1, 0
    for i, c in enumerate(text, 1):
        if c == '\n':
            print(text[j:i].strip(), end='')
            j = i
        elif c in ('.', '?', ':'):
            print(text[j:i].strip(), end="\n\n")
            j = i
    if i != j:
        print(text[j:i].strip(), end='')
