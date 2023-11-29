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
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not all(isinstance(item, (int, float)) for item in matrix[i]):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    #return new matrix
    return [[round(a / div, 2) for a in row] for row in matrix]
