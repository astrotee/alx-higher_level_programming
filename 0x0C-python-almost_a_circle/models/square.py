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
        if len(args) > 1:
            nargs = args[:2] + args[1:]
        else:
            nargs = args
        nkwargs = kwargs
        if "size" in kwargs:
            nkwargs["width"] = kwargs["size"]
            nkwargs["height"] = kwargs["size"]
            del nkwargs["size"]

        super().update(*nargs, **nkwargs)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
