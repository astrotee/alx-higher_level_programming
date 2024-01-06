#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not isinstance(matrix, list):
        return
    for r in matrix:
        if not isinstance(r, list):
            return
        print('{:d}'.format(' '.join(r)))
