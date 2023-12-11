import sys
import numpy as np
from itertools import product

def expand_grid(grid):
    new_grid = grid.copy()
    row = 0
    while row < new_grid.shape[0]:
        if np.all(new_grid[row,:] == '.'):
            print('inserting row')
            new_grid = np.insert(new_grid, row, '.', axis=0)
            row += 1
        row += 1

    col = 0
    while col < new_grid.shape[1]:
        if np.all(new_grid[:,col] == '.'):
            print('inserting col')
            new_grid = np.insert(new_grid, col, '.', axis=1)
            col += 1
        col += 1

    return new_grid

def main():
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])

    grid = expand_grid(grid)

    galaxies = [(row,col) for (row,col) in product(range(grid.shape[0]), range(grid.shape[1])) if grid[row][col] == '#']
    print(galaxies)

main()
