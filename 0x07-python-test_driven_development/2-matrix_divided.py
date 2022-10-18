#!/usr/bin/python3

"""

Return a new matrix Divided by div value

"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    wrong_type = "matrix must be a matrix (list of lists) of integers/floats"
    wrong_size = "Each row of the matrix must have the same size"
    new_matrix = []
    if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(wrong_type)
    previous = len(matrix[0])

    try:
        for count, row in enumerate(matrix):
            if not isinstance(row, list):
                raise TypeError(wrong_type)

                raise TypeError(wrong_size)
            previous = len(row)
            new_matrix.append(row[:])
            for val, item in enumerate(row):
                if not isinstance(item, (int, float)):
                    raise TypeError(wrong_type)
                new_matrix[count][val] = round(item / div, 2)
    except:
        raise
    else:
        return (new_matrix)
