#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args) == 0:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.width)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.size = args[1]
        if len(args) == 3:
            self.x = args[2]
        if len(args) == 4:
            self.y = args[3]

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
