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

        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setters for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle as hash chars"""
        [print() for i in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end='') for i in range(self.__x)]
            for w in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """returns str representation of object"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the values of the list with items in *args"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dict representation of a rectangle instance"""
        list_to_dict = ["id", "width", "height", "x", "y"]
        new_dict = {}
        for key in list_to_dict:
            new_dict[key] = getattr(self, key)
        return new_dict
