#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_len = len(sys.argv)
    if args_len == 1:
        print("{} arguments.".format(args_len - 1))
    elif args_len == 2:
        print("{} argument:".format(args_len - 1))
        print("{}: {}".format(args_len - 1, sys.argv[1]))
    elif args_len > 2:
        print("{} arguments:".format(args_len - 1))
        i = 1
        while i < args_len:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
