#!/usr/bin/python3
"""define a Square class"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initialize the size"""
        self.__size = size

    def area(self):
        """the area of the square"""
        return self.__size**2

    @property
    def size(self):
        """the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
