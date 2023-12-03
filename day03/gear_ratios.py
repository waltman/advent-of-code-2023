from sys import argv
import numpy as np
import re

def is_part_num(grid, row, start_col, end_col):
    return any([re.search(r'[^\d\.]', ''.join(grid[row-1, start_col-1:end_col+2])),
                re.search(r'[^\d\.]', ''.join(grid[row,   [start_col-1,end_col+1]])),
                re.search(r'[^\d\.]', ''.join(grid[row+1, start_col-1:end_col+2]))]
               )

# read in the grid
with open(argv[1]) as f:
    input_grid = [line.rstrip() for line in f]
    rows = len(input_grid)
    cols = len(input_grid[0])

# put it into a np array with one row/col of buffer all around it
grid = np.array(['.'] * (rows+2) * (cols+2)).reshape([rows+2, cols+2])
for row in range(rows):
    grid[row+1, 1:cols+1] = [c for c in input_grid[row]]
rows += 2
cols += 2

# now look for numbers in the grid
part1 = 0
for row in range(1, rows-1):
    col = 1
    start_col = -1
    while col < cols:
        if grid[row,col].isdigit():
            if start_col == -1:
                start_col = col
                val = int(grid[row,col])
            else:
                val = val * 10 + int(grid[row,col])
        else:
            if start_col != -1:
                if is_part_num(grid, row, start_col, col-1):
                    part1 += val
                start_col = -1
                val = -1
        col += 1
        
print('Part 1:', part1)



