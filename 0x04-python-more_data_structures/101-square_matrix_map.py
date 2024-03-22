#!/usr/bin/python3

def square_matrix_simple_map(matrix=[]):
    # Define a function to square a single value
    def square(x):
        return x ** 2

    squared_matrix = list(map(lambda row: list(map(square, row)), matrix))

    return squared_matrix
