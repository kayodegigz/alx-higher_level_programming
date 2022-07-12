#!/usr/bin/python3
"""Module contains a class that defines a rectangle"""
from base import Base


class Rectangle(Base):
    """Class defines rectangle prop. and inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialising values of the instance"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        Super.__init__(self, id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__x

    @y.setter
    def y(self, y):
        self.__y = y
