#!/usr/bin/python3

"""Module contains a func that appends text to a file"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
