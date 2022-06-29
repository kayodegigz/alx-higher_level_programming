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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width != 0 and self.__height != 0:
            return (2 * (self.__width + self.__height))
        return 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        new_list = []
        for i in range(self.__height):
            for j in range(self.__width):
                new_list.append("#")

            if i < self.__height - 1:  # dat is if idx isn't @ d rect lastline
                new_list.append("\n")
        return "".join(new_list)

    def __repr__(self):
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"
