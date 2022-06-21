#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        func_ret = fct(*args)
        return func_ret
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
