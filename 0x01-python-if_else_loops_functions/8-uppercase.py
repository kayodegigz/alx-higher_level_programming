#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for letter in str:
        ascii_val = ord(letter)

        if ascii_val not in range(97, 123):
            new_str += letter
        else:
            ascii_val_upper = ascii_val - 32
            new_char = chr(ascii_val_upper)
            new_str += new_char
    print("{}".format(new_str))
