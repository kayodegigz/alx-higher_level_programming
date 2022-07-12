#!/usr/bin/python3

def matrix_divided(matrix, div):
    i = 0
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")
    for row in matrix:
        for num in row:
            if not isinstance(num, int) or not isinstance(num, float):
                raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    while i < len(matrix):
        if len(matrix[i]) is not == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1
    if not isinstance(div, int) or not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_num = num/div
            new_row.append(new_num)
        new_matrix.append(row)
    return new_matrix
