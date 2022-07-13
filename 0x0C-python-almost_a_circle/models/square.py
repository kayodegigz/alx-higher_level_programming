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
