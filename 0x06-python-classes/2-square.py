#!/usr/bin/python3


"""A class that defines a square"""


class Square:
    def __init__(self, size=0):
        """instantiating Size of square is a hidden var
            and must be a positive int
        Args:
            size(int): The size of the square
        """
        if typeof(__size) is not int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
