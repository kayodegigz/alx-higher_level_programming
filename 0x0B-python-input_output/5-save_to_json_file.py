#!/usr/bin/python3
import json

"""module writes a json obj into a txt file"""


def save_to_json_file(my_obj, filename):
    """writes json obj into a txt file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
