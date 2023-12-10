import sys
import numpy as np

def start_pos(grid):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row][col] == 'S':
                return row, col

with open(sys.argv[1]) as f:
    grid = np.array([[c for c in line.rstrip()] for line in f])

print(start_pos(grid))
