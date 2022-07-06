#!/usr/bin/python3
"""module contains a class Student"""


class Student:
    """A student class that contains the following attr"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """So what I did here is I first checked if attrs is a list,
        also if all the items in the list are strs, once that has been
        established, a new dict is initialised, then we loop thru the list
        , check if item in the string(item) is an attribute of the instance
        , if it is just get the attr value and add it as a value to the dict,
        the key would be the item name
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
                new_dict = {}
                for item in attrs:
                    if hasattr(self, item):
                        new_dict[item] = getattr(self, item)
                return new_dict
        return self.__dict__
