#!/usr/bin/python3
def remove_char_at(str, n):
    for x in str:
        if x != str[n]:
            new_str += x
    return new_str
