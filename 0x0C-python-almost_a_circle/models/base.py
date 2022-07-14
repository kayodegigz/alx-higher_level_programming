#!/usr/bin/python3
"""module contains a class that defines a base"""
import json
import csv


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
        """changes a jsonstr to python objs"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from a dict"""
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
        """loads from a json file"""
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """gets list of objs, converts to l of dicts amd writes to csv file"""
        filename = cls.__name__ + ".csv"
        list_of_dicts = []
        with open(filename, "w", encoding="utf-8") as csv_f:
            field_name_keys = []
            for obj in list_objs:
                list_of_dicts.append(cls.to_dictionary(obj))
            for key in list_of_dicts[0].keys():
                """looping thru d keys of the 1st dict to get the
                field names since the keys serve as field names in
                csv files"""
                field_name_keys.append(key)
            writer = csv.DictWriter(csv_f, fieldnames=field_name_keys)
            writer.writeheader()
            writer.writerows(list_of_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """loads from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as csv_f:
                list_of_inst = []
                reader = csv.DictReader(csv_f)
                list_of_dicts = list(reader)

                """new_dict will hold the int version of values
                in the dict d cos they're in str format from the csv file"""
                new_dict = {}
                for d in list_of_dicts:
                    for key, value in d.items():
                        new_dict[key] = int(value)
                    list_of_inst.append(cls.create(**new_dict))
                return list_of_inst
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
