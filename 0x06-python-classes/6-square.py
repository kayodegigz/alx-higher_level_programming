#!/usr/bin/python3


"""A class that defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiating Size of square is a hidden var
            and must be a positive int
        Args:
            size(int): The size of the square
        """
        self.__size = size
        self.__position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square on the terminal"""
        if self.__size == 0:
            print()

        [print("", end="") for r in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for n in range(self.__position[0])]
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """gets the value of the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position equal to a particular value
        Args:
            value(int): the value position will be set to
        """
        if (value[0] < 0 and value[1] < 0 or 
                len(value) != 2
                or not(isinstance(value[0], int) and isinstance(value[1], int))
                or not(isinstance(value, tuple))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
