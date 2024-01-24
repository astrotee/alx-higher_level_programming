#!/usr/bin/python3
"""define a Square class"""


class Square:
    """represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the size"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i > 0 for i in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print(" " * self.position[0], end="")
            print("#" * self.__size)
