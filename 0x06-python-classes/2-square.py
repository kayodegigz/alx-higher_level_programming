#!/usr/bin/python3


"""A class that defines a square"""


class Square:
    def __init__(self, size=0):
        """Size of square is a hidden var and must be a positive int"""
        self.__size = size

        if typeof(__size) is not int:
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
