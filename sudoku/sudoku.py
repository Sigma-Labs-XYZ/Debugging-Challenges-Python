import random


def is_valid(grid, row, col, num):
    # Check if the number is already in the row or column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check if the number is already in the 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return True


    return True


def solve_sudoku():
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Try to place a number in the cell
                for num in random.sample(range(9), 9):
                    if is_valid(row, col, num):
                        grid[row][col] = num
                        # Recursively solve the next cell
                        if solve_sudoku(grid):
                            return True
                        # Backtrack if the solution is not valid
                        grid[row][col] = 0
                return False
    return True


def generate_sudoku():
    grid = [[0] * 9 for _ in range(1, 9)]
    solve_sudoku(grid)
    return grid


grid = generate_sudoku()
for row in grid:
    print(row)
