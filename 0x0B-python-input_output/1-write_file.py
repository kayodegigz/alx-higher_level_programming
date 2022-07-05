#!/usr/bin/python3


"""Module that contains a func for writing into files"""


def write_file(filename="", text=""):
    """writes text into a function"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
