#!/usr/bin/python3
"""module defines a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class defines a square that inherits from a rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialisation constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str format constructor"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes with args or kwargs"""
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
