#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        new_row = []
        for num in item:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
