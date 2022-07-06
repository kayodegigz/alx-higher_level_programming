#!/usr/bin/python3
"""module creates a dict reoresentation of a python obj"""


def class_to_json(obj):
    """returns the dict description of an object"""
    return obj.__dict__
