#!/usr/bin/python3
"""module contains a class that defines a base"""
import json


class Base:
    """A class that contains definitions for a base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of dictionaries in a list"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objs in json format to a file"""
        with open(cls.__name__.json, "w", encoding="utf-8") as j_file:
            if list_objs is None:
                j_file.write([])
            else:
                json_str = cls.to_json_string(list_objs)
                j_file.write(json_str)
