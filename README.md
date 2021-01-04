# Sudoku Solver
This is a simple sudoku solver that will attempt to solve any n*n sudoku grid.

## How to Use
1. Create a file called **puzzle.txt** (one is already included in the repository).
2. In the text file, insert a *space-separated* list of integers for each row - one per line.
3. Run the Python script. The larger the grid, the longer the solver will take.

## Example Text File
    3 0 0 1
    1 0 2 4
    0 0 0 3
    0 1 0 0
    
Running the script with this text file will yield the following solution:

    [3, 2, 4, 1]
    [1, 3, 2, 4]
    [2, 4, 1, 3]
    [4, 1, 3, 2]
