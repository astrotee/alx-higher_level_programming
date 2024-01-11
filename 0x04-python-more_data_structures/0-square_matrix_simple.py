#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    square_matrix = list()
    for r in matrix:
        square_matrix.append(list(map(lambda x: x*x, r)))
    return square_matrix
