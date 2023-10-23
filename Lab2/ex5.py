# Function to replace elements under the main diagonal with zeros in a matrix
def replace_below_diagonal_with_zeros(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j] = 0
    return matrix

# Example input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function and print the result
modified_matrix = replace_below_diagonal_with_zeros(matrix)
for row in modified_matrix:
    print(row)
