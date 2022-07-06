#!/usr/bin/python3
"""module is a script that encodes python objects to json and saves"""

import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:  # check if file exists by trying to load its contents
        new_list = load_from_json_file("add_item.json")
    except FileNotFoundError:  # if it doesn't exist init a fresh list
        new_list = []
    new_list.extend(sys.argv[1:])
    save_to_json_file(new_list, "add_item.json")
