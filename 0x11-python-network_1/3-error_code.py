#!/usr/bin/python3
"""
    a Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""

import urllib.request
import sys

url = sys.argv[1]

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
