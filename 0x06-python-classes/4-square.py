#!/usr/bin/python3


"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """instantiating Size of square is a hidden var
            and must be a positive int
        Args:
            size(int): The size of the square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        return self.__size

    @setter.size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square"""
        return self.__size ** 2
