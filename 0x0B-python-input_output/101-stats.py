#!/usr/bin/python3
"""module parses lines from stdin"""


import sys


def print_status():
    """prints the status of log files as well as size"""

    counter = 0
    size = 0
    status_codes = {"200": 0, "301": 0, "400": 0,
                    "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    for line in sys.stdin:
        counter += 1
        line_list = line.split()
        try:
            size += int(line_list[-1])
            code = line_list[-2]
            status_codes[code] += 1
        except Exception:
            continue

        if counter == 10:
            print("File size: {}".format(size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            counter = 0
        # counter += 1

    if counter < 10:
        print("File size: {}".format(size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))


if __name__ == "__main__":
    print_status()
