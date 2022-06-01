#!/usr/bin/python3
for x in range(1, 100):
    if x == 89:
        print(x)
        break
    if x < 10:
        print("{:0>2d}, ".format(x), end="")
    elif (x % 10) > (x // 10):
        print("{}, ".format(x), end="")
