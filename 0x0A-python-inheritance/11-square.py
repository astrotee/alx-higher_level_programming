#!/usr/bin/python3
"""Geometry Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate the area"""
        return self.__size**2

    def __str__(self) -> str:
        return f"[Square] {self.__size}/{self.__size}"
