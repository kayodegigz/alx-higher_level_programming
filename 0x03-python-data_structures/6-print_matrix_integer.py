#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0 #initialize i inside the loop again so the value is reset
        for r in row:
            row_len = len(row) - 1
            if i < row_len:
                print("{:d}".format(r), end=" ")
            else:
                print("{:d}".format(r))
            i += 1
