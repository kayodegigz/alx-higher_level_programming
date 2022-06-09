#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        for num in item:
            new_matrix.append(num ** 2)
    return new_matrix
