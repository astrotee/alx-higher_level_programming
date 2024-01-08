#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not isinstance(matrix, list):
        return
    for r in matrix:
        if not isinstance(r, list):
            return
        for c in r:
            print('{}'.format(c), end="")
            if c != r[-1]:
                print(" ", end="")
        print()
