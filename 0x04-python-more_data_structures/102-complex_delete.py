#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.items():
        if v == value:
            return a_dictionary.pop(k)
        else:
            return a_dictionary
