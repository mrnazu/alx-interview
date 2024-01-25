#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    matrix = []
    if n <= 0:
        return matrix
    matrix = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(matrix[i - 1]) - 1):
            curr = matrix[i - 1]
            temp.append(matrix[i - 1][j] + matrix[i - 1][j + 1])
        temp.append(1)
        matrix.append(temp)
    return matrix
