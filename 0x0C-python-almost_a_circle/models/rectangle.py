#!/usr/bin/python3
"""Module contains a class that defines a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class defines rectangle prop. and inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialising values of the instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Super().__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__x

    @y.setter
    def y(self, value):
        self.__y = value
