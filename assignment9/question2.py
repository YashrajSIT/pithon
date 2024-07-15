def find_character(matrix, char):
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):
            if element == char:
                print(f"Found at row {row_index}, column {col_index}")
                return
    print("Not found")

# Input the matrix from the user
matrix = []
rows = int(input("Enter the number of rows in the matrix: "))
for i in range(rows):
    row = input(f"Enter row {i} elements separated by spaces: ").split()
    matrix.append(row)

# Input the character to search for
char = input("Enter the character to search for: ")

# Call the function
find_character(matrix, char)