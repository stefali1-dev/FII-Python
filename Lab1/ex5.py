# Function to print the spiral order of characters from a square matrix
def print_spiral_order(matrix):
    if not matrix:
        return ""

    result = []
    while matrix:
        # Traverse the top row
        result.extend(matrix[0])
        matrix = list(zip(*matrix[1:]))[::-1]  # Rotate the matrix counterclockwise
    return ''.join(result)

# Example square matrix
matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

# Call the function and print the result
result_string = print_spiral_order(matrix)
print(result_string)
