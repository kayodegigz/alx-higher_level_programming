#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a != () and tuple_b != ():
        if len(tuple_a) < 2:
            new_tuple_a = (tuple_a[0], 0)
        elif len(tuple_a) > 1:
            new_tuple_a = tuple_a

        if len(tuple_b) < 2:
            new_tuple_b = (tuple_b[0], 0)
        elif len(tuple_b) > 1:
            new_tuple_b = tuple_b

        s = (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])

    if tuple_a == () and tuple_b == ():  # if 2 tuples are empty
        s = (0, 0)

    elif tuple_a == ():
        s = (tuple_b[0], tuple_b[1])
    elif tuple_b == ():
        s = (tuple_a[0], tuple_a[1])
    return s
