from copy import copy
from itertools import product


def is_distinct(lst: list) -> bool:
    """Determine whether or not all of the numbers in a row or column are unique."""
    used = []
    for i in lst:
        # Skip zeroes.
        if i == 0:
            continue
        # Check if i has already been used.
        if i in used:
            return False
        used.append(i)
    # If all of the numbers are distinct, return True.
    return True


def validate(grid: list) -> bool:
    """Validate the rows and columns on a sudoku grid."""
    for i in range(len(grid)):
        # Get the row and column.
        row = [grid[i][j] for j in range(len(grid[i]))]
        if not is_distinct(row):
            return False
        # Check whether the row contains distinct numbers.
        col = [grid[j][i] for j in range(len(grid[i]))]
        # Check whether the column contains distinct numbers.
        if not is_distinct(col):
            return False
    return True


def count_blanks(grid: list) -> int:
    """Count the number of blank spaces (denoted by 0) on the sudoku grid."""
    blanks = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                blanks += 1

    return blanks


def solve(grid: list, blanks=81):
    """Solves a n*n sudoku grid in the form of a nested list."""
    # Base case.
    if blanks == 0:
        return validate(grid)
    # Iterate through every cell.
    for row, col in product(range(len(grid)), repeat=2):
        cell = grid[row][col]
        # If cell is not blank, then jump to the next cell.
        if cell != 0:
            continue
        # Create a shallow copy of the grid.
        grid2 = copy(grid)
        # Try 0-9 for the cell values.
        for candidate in range(1, len(grid)+1):
            grid2[row][col] = candidate
            if validate(grid2) and solve(grid2, blanks-1):
                return True
            # Backtrack
            grid2[row][col] = 0
    return False


if __name__ == '__main__':
    # Test case.
    puzzle = []
    # Read the puzzle from the file.
    file = 'puzzle.txt'
    with open(file) as f:
        for line in f.read().split('\n'):
            puzzle.append([int(n) for n in line.split()])

    # Solve the puzzle.
    print("Solved." if solve(puzzle, count_blanks(puzzle)) else "Cannot be solved.")
    for row in puzzle:
        print(row)
