import sys
import numpy as np
from itertools import product, combinations

def expand_grid(grid):
    new_grid = grid.copy()
    row = 0
    while row < new_grid.shape[0]:
        if np.all(new_grid[row,:] == '.'):
            new_grid = np.insert(new_grid, row, '.', axis=0)
            row += 1
        row += 1

    col = 0
    while col < new_grid.shape[1]:
        if np.all(new_grid[:,col] == '.'):
            new_grid = np.insert(new_grid, col, '.', axis=1)
            col += 1
        col += 1

    return new_grid

def expand_galaxies(grid, val):
    galaxies = [[row,col] for (row,col) in product(range(grid.shape[0]), range(grid.shape[1])) if grid[row][col] == '#']
    for row in range(grid.shape[0]-1, -1, -1):
        if np.all(grid[row,:] == '.'):
            for galaxy in galaxies:
                if galaxy[0] > row:
                    galaxy[0] += val

    for col in range(grid.shape[1]-1, -1, -1):
        if np.all(grid[:,col] == '.'):
            for galaxy in galaxies:
                if galaxy[1] > col:
                    galaxy[1] += val

    return galaxies

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def main():
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])

    galaxies = expand_galaxies(grid, 1)
    print('Part 1:', sum([dist(p1, p2) for (p1, p2) in combinations(galaxies, 2)]))
    galaxies = expand_galaxies(grid, 999_999)
    print('Part 2:', sum([dist(p1, p2) for (p1, p2) in combinations(galaxies, 2)]))

main()
