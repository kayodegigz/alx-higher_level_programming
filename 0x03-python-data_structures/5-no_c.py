#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if letter == c or letter == C:
            my_string.remove(letter)
        return my_string
