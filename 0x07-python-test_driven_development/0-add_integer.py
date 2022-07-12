#!/usr/bin/python3
"""module adds two variables that have to be ints"""


def add_integer(a, b):
    """adds two integers a and b while handling exceptions"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
