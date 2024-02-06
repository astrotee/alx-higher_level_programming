#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """my custom list class"""

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
