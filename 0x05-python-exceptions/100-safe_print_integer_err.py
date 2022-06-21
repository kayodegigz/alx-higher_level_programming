#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as v:
        print("Exception: {}".format(v.__str__), file = sys.stderr) 
        # above __str__ prints only err msg without the err type
        return False
    except TypeError as t:
        print("Exception: {}".format(t.__str__), file = sys.stderr)
        return False

