#!/usr/bin/python3
"""module defines a function"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.

    Args:
        matrix : list of lists of integers or floats
        div : int or float

    Returns
        a new matrix

    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for item in matrix:
        if not isinstance(item, list) or len(item) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(item) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for a in item:
            if not isinstance(a, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


        #return new matrix
    return [[round(a / div, 2) for a in item] for item in matrix]
