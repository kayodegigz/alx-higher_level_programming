#!/usr/bin/python3

"""module writes a json obj into a txt file"""

import json


def save_to_json_file(my_obj, filename):
    """writes json obj into a txt file
    Args:
        @my_obj: the object to be encoded
        @filename: name of the txt file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
