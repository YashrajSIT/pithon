def determinant_2x2(matrix):
    """Calculate and return the determinant of a 2x2 matrix."""
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix")

    a, b = matrix[0]
    c, d = matrix[1]
    
    return a * d - b * c

def get_user_input():
    """Get a 2x2 matrix from user input."""
    matrix = []
    print("Enter the elements of the 2x2 matrix row by row:")
    
    for i in range(2):
        row = input(f"Enter row {i + 1} (two space-separated integers): ").split()
        if len(row) != 2:
            raise ValueError("Each row must contain exactly two integers.")
        row = [int(num) for num in row]
        matrix.append(row)
    
    return matrix

# Example usage:
try:
    user_matrix = get_user_input()
    det = determinant_2x2(user_matrix)
    print(f"Determinant of the matrix is: {det}")
except ValueError as e:
    print(f"Error: {e}")