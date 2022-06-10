#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_list = []
    for k, v in a_dictionary.items():
        if v == value:
            a_list.append(k)  # list of keys to be removed

    for key in a_list:
        a_dictionary.pop(key, None)
    return a_dictionary
