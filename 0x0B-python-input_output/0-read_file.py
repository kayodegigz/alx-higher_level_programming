#!/usr/bin/python3


"""reads all contents of a file"""


def read_file(filename=""):
    """function reads all the content of a file"""
    with open("filename", encoding="UTF8") as f:
        print(f.read())
