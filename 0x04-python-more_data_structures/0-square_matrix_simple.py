#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    return [[col**2 for col in row] for row in matrix]
