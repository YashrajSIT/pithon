def matrix_multiplication(A, B):
    # Get the dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Cannot multiply the two matrices. Number of columns in A must be equal to number of rows in B.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform the multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example input
A = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

# Perform matrix multiplication
result = matrix_multiplication(A, B)

# Print the result
for row in result:
    print(row)