import sys
import numpy as np
from collections import defaultdict, deque

def entrance(grid):
    for col in range(grid.shape[1]):
        if grid[0,col] == '.':
            return (0, col)

def door(grid):
    nrows = grid.shape[0]
    for col in range(grid.shape[1]):
        if grid[nrows-1, col] == '.':
            return (nrows-1, col)

def valid_moves(position, grid):
    row, col = position
    nrows, ncols = grid.shape
    square = grid[row, col]
    if square == '<':
        yield row, col-1
    elif square == '>':
        yield row, col+1
    elif square == '^':
        yield row-1, col
    elif square == 'v':
        yield row+1, col
    elif square == '.':
        if row > 0 and grid[row-1, col] != '#':
            yield row-1, col
        if row < nrows-1 and grid[row+1, col] != '#':
            yield row+1, col
        if col > 0 and grid[row, col-1] != '#':
            yield row, col-1
        if col < ncols-1 and grid[row, col+1] != '#':
            yield row, col+1

def valid_moves2(position, grid):
    row, col = position
    nrows, ncols = grid.shape
    if row > 0 and col < ncols-1 and grid[row-1, col]:
        yield row-1, col
    if row < nrows-1 and grid[row+1, col]:
        yield row+1, col
    if col > 0 and row < nrows-1 and grid[row, col-1]:
        yield row, col-1
    if col < ncols-1 and grid[row, col+1]:
        yield row, col+1

def main():
    # read in the grid
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])
    nrows, ncols = grid.shape

    stack = []
    stack.append((entrance(grid), set()))
    worst = 0
    maze_exit = door(grid)
    while stack:
        position, seen = stack.pop()
        if position == maze_exit:
            if len(seen) > worst:
                print('new worst', len(seen))
                worst = len(seen)
        elif position not in seen:
            for new_pos in valid_moves(position, grid):
                stack.append((new_pos, seen | {position}))
    print('Part 1:', worst)

    grid2 = np.zeros(grid.shape, dtype=bool)
    for row in range(nrows):
        for col in range(ncols):
            if grid[row,col] != '#':
                grid2[row,col] = True

    stack = []
    stack.append((entrance(grid), set()))
    worst = 0
    maze_exit = door(grid)
    while stack:
        position, seen = stack.pop()
        if position == maze_exit:
            if len(seen) > worst:
                print('new worst', len(seen))
                worst = len(seen)
            # else:
            #     print('found path of length', len(seen))
        elif position not in seen:
            for new_pos in valid_moves2(position, grid2):
                if new_pos not in seen:
                    stack.append((new_pos, seen | {position}))
    print('Part 2:', worst)
    
main()
