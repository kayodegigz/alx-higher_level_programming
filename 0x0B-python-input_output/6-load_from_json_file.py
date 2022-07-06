#!/usr/bin/python3
"""module creates an object from a json file"""

import json


def load_from_json_file(filename):
    """Func returns a py object from a json file"""
    with open(filename, "r") as f:
        return json.load(f)
