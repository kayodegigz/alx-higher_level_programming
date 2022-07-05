#!/usr/bin/python3

"""Module contains a func that returns json encoding of a str"""

import json


def to_json_string(my_obj):
    """functions that returns the encided json object"""
    return json.dumps(my_obj)
