#!/usr/bin/python3
"""divide a matrix by a number"""


def matrix_divided(matrix, div):
    """divide matrix by div"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    new_mat = list()
    size = None
    for r in matrix:
        if not isinstance(r, list):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if size is None:
            size = len(r)
        elif size != len(r):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = list()
        for c in r:
            if not isinstance(c, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_row.append(round(c / div, 2))
        new_mat.append(new_row)
    return new_mat
