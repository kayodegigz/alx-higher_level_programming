#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0

    if my_list == []:
        return None
    while i < len(my_list) - 1:  # so that last index won't be OOR
        if my_list[i] > my_list[i + 1]:
            my_list[i + 1] = my_list[i]
        i += 1
    return my_list[i]
