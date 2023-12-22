import sys
import numpy as np
from collections import deque

def do_empty(dir):
    if dir == 'r':
        return 0, 1, 'r'
    elif dir == 'l':
        return 0, -1, 'l'
    elif dir == 'u':
        return -1, 0, 'u'
    elif dir == 'd':
        return 1, 0, 'd'

def do_slash(dir): # /
    if dir == 'r':
        return do_empty('u')
    elif dir == 'l':
        return do_empty('d')
    elif dir == 'u':
        return do_empty('r')
    elif dir == 'd':
        return do_empty('l')

def do_backslash(dir): # \
    if dir == 'r':
        return do_empty('d')
    elif dir == 'l':
        return do_empty('u')
    elif dir == 'u':
        return do_empty('l')
    elif dir == 'd':
        return do_empty('r')

def do_dash(dir): # -
    if dir in {'u', 'd'}:
        yield do_empty('l')
        yield do_empty('r')
    else:
        yield do_empty(dir)

def do_vert(dir): # |
    if dir in {'r', 'l'}:
        yield do_empty('u')
        yield do_empty('d')
    else:
        yield do_empty(dir)

def trace_beam(grid, row, col, dir):
    nrows, ncols = grid.shape
    energized = set()
    seen = set()
    queue = deque()
    queue.append((row, col, dir))
    while queue:
        row, col, dir = queue.popleft()

        # is the point in the grid?
        if row < 0 or row >=nrows or col < 0 or col >= ncols:
            continue

        # have we been here before?
        if (row, col, dir) in seen:
            continue
        else:
            seen.add((row, col, dir))
            energized.add((row, col))

        # move to the next point
        if grid[row][col] == '.':
            drow, dcol, dir = do_empty(dir)
            queue.append((row+drow, col+dcol, dir))
        elif grid[row][col] == '/':
            drow, dcol, dir = do_slash(dir)
            queue.append((row+drow, col+dcol, dir))
        elif grid[row][col] == '\\':
            drow, dcol, dir = do_backslash(dir)
            queue.append((row+drow, col+dcol, dir))
        elif grid[row][col] == '-':
            for drow, dcol, dir in do_dash(dir):
                queue.append((row+drow, col+dcol, dir))
        elif grid[row][col] == '|':
            for drow, dcol, dir in do_vert(dir):
                queue.append((row+drow, col+dcol, dir))

    return len(energized)

def gen_coords(grid):
    nrows, ncols = grid.shape

    # vertical
    for col in range(ncols):
        yield(0, col, 'd')
        yield(nrows-1, col, 'u')

    # horizontal
    for row in range(nrows):
        yield(row, 0, 'r')
        yield(row, ncols-1, 'l')

def main():
    # read in the grid
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])
            
    print('Part 1:', trace_beam(grid, 0, 0, 'r'))
    print('Part 2:', max([trace_beam(grid, row, col, dir) for row, col, dir in gen_coords(grid)]))

main()
