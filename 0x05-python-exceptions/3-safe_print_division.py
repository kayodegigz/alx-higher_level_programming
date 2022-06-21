#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a/b
    except ZeroDivisionError:
        return None
    finally:
        print("{}".format(div))
        return div
