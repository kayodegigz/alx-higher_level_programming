#!/usr/bin/python3
"""
    a Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""

import sys
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    response = requests.post(url, data={'q': letter})
    try:
        r_dict = response.json()
        
        if r_dict:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
