# Function to find seats where spectators can't see the game
def find_obstructed_seats(matrix):
    obstructed_seats = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            height = matrix[i][j]
            for k in range(i + 1, rows):
                if matrix[k][j] >= height:
                    obstructed_seats.append((k, j))

    return obstructed_seats

# Example input (stadium heights)
stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

# Call the function and print the result
obstructed_seats = find_obstructed_seats(stadium)
print(obstructed_seats)
