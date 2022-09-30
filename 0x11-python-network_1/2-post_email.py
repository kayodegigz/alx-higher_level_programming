#!/usr/bin/python3

"""A script that:

    - takes in a URL

    - sends a POST request to the passed URL

    - takes email as a parameter

    - displays the body of the response

    """

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]

    value = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(request) as response:
            if response:
                print(response.read().decode("utf-8"))
    except BaseException:
        pass
