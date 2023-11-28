#!/usr/bin/python3
def pascal_triangle(n):

    # Initializes an empty list named 'matrix'. This list will be used to store the rows of Pascal's Triangle.
    matrix = []

    # Checks if the input 'n' is less than or equal to 0. 
    # If true, it returns an empty list because Pascal's Triangle is not defined for non-positive values of 'n'.
    if n <= 0:
        return matrix # empty matrix list
    
    matrix = [[1]] # Initializes 'matrix' with the first row of Pascal's Triangle, which is always 'row n = 1'.

    # Initiates a loop that starts from '1' (since the first row is already initialized) and goes up to (but not including) 'n'. 
    # This loop generates the subsequent rows of Pascal's Triangle.
    for i in range(1, n):
        temp = [1] # Initializes a temporary list temp with the first element of each row, which is always 1.

        # Initiates a loop that iterates through the elements of the previous row (the row above the current one).
        for j in range(len(matrix[i - 1]) - 1):
            curr = matrix[i - 1]

            # Calculates and appends the next element in the row by summing the corresponding elements from the previous row.
            temp.append(matrix[i - 1][j] + matrix[i - 1][j + 1])
        temp.append(1)
        matrix.append(temp)
    return matrix
