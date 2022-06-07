#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 1 or idx > (len(my_list) - 1):
        return my_list
    i = 0
    new_list = []
    while i < len(my_list):
        if i == idx:
            pass
        else:
            new_list.append(my_list[i])
    my_list = new_list            
    return new_list
