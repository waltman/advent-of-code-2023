import sys
import numpy as np

def slide_north(grid):
    nrows, ncols = grid.shape
    for row in range(1, nrows):
        for col in range(0, ncols):
            if grid[row][col] == 'O':
                for r1 in range(row-1, -1, -1):
                    if grid[r1][col] == '.':
                        grid[r1][col] = 'O'
                        grid[r1+1][col] = '.'
                    else:
                        break

def total_load(grid):
    nrows, ncols = grid.shape
    load = 0
    for row in range(nrows):
        for col in range(ncols):
            if grid[row][col] == 'O':
                load += nrows - row

    return load

def main():
    # read in the grid
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line] for line in f])

    slide_north(grid)
    print('Part 1:', total_load(grid))

main()
