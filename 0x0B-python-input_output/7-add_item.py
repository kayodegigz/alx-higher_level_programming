#!/usr/bin/python3
"""module is a script that encodes python objects to json and saves"""

import sys


if __name__ == "__main__":
    load_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_json_file = __import__('5-save_to_json_file').save_to_json_file


    try:  # check if file exists by trying to load its contents
        new_list = load_json_file("add_item.json")
    except FileNotFoundError:  # if it doesn't exist init a fresh list
        new_list = []
    for arg in sys.argv[1:]:
        new_list.append(arg)
    save_json_file(new_list, "add_item.json")
