#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """represents a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if 0 in (self.width, self.height):
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        if 0 in (self.width, self.height):
            return ""
        return "\n".join(['#' * self.width] * self.height)
