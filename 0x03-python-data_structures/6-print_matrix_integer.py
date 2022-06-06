#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for r in row:
            print("{:d}".format(r), end=" ")
        print("\n")
