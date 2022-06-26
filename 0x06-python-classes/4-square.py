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
        self.size = size

    @property
    def size(self):
        """getter that retrieves the value of the attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the attribute size equal to value
        Args:
            value(int): The value that the attribute will be set to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square"""
        return self.__size ** 2
