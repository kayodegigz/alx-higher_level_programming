#!/usr/bin/python3
"""Module contains func that decodes a json obj to a python obj"""

import json


def from_json_string(my_str):
    """returns a decoded json obj"""
    return json.loads(my_str)
