#!/usr/bin/python3
"""Base class"""

from models.base import Base


class Rectangle(Base):
    """represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the area"""
        return self.width * self.height

    def display(self):
        """display the rectangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
        if self.height == 0:
            print()

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args) == 0:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.width = args[1]
        if len(args) == 3:
            self.height = args[2]
        if len(args) == 4:
            self.x = args[3]
        if len(args) == 5:
            self.y = args[4]

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
                f" - {self.width}/{self.height}"
