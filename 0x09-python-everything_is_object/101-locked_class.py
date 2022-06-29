#!/usr/bin/python3

"""Module contains a class"""


class LockedClass:
    """The class does not allow dynamic creation of new attributes"""
    __slots__ = ["first_name"]
