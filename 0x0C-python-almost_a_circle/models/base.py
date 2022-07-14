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
        filename = cls.__name__ + ".json"
        list_dict = []
        with open(filename, "w", encoding="utf-8") as j_file:
            if list_objs is None:
                j_file.write("[]")
            else:
                for obj in list_objs:
                    """append each object represented as a dict to list_dict"""
                    list_dict.append(obj.to_dictionary())
                json_str = cls.to_json_string(list_dict)
                j_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r = Rectangle(3, 2)
        elif cls.__name__ == "Square":
            r = Square(11)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_of_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []

        new_list = []
        for d in list_of_dicts:
            new_list.append(cls.create(**d))
        return new_list
