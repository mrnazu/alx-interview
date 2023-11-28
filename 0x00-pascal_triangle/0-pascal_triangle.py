def pascal_triangle(n): # n = rows of triangles or number of rows
    matrix = [] # for storing rows

    # now to iterate rows "n"(ex. 4) times we need for loop.
    for x in range(n):
        rows = []

        for y in range(x + 1):
            result = combination(x , y)

            rows.append(result) # append results to the rows

        matrix.append(rows) # append rows to the matrix

    return matrix # return the matrix
    
