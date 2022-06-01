#!/usr/bin/python3
for x in range(97, 123):
    if x == 101 or x == 113:
        pass
    else:
        char_x = chr(x)
        print("{}".format(char_x), end="")
