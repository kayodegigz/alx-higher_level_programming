#!/usr/bin/python3

"""a module that contains a rectangle class"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """initialising values of instances
        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieving the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of the width == value
        Args:
            value(int): value must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieving the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the value of the height == value
        Args:
            value(int): value must be an int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise VakueError("height must be >= 0")
        self.__height = value
