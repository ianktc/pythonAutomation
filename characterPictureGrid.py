# program to rotate the list into a heart (90 degrees)
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotate(grid):
    # uses for loop to print each column as row (notice switching of i and j elements during printing)
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end = '')
        print()

rotate(grid)
