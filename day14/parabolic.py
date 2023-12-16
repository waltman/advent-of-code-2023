import sys
import numpy as np

def slide_north(grid):
    nrows, ncols = grid.shape
    for row in range(1, nrows):
        for col in range(ncols):
            if grid[row][col] == 'O':
                for r1 in range(row-1, -1, -1):
                    if grid[r1][col] == '.':
                        grid[r1][col] = 'O'
                        grid[r1+1][col] = '.'
                    else:
                        break

def slide_south(grid):
    nrows, ncols = grid.shape
    for row in range(nrows-2, -1, -1):
        for col in range(ncols):
            if grid[row][col] == 'O':
                for r1 in range(row+1, nrows):
                    if grid[r1][col] == '.':
                        grid[r1][col] = 'O'
                        grid[r1-1][col] = '.'
                    else:
                        break

def slide_west(grid):
    nrows, ncols = grid.shape
    for col in range(1, ncols):
        for row in range(nrows):
            if grid[row][col] == 'O':
                for c1 in range(col-1, -1, -1):
                    if grid[row][c1] == '.':
                        grid[row][c1] = 'O'
                        grid[row][c1+1] = '.'
                    else:
                        break

def slide_east(grid):
    nrows, ncols = grid.shape
    for col in range(ncols-2, -1, -1):
        for row in range(nrows):
            if grid[row][col] == 'O':
                for c1 in range(col+1, ncols):
                    if grid[row][c1] == '.':
                        grid[row][c1] = 'O'
                        grid[row][c1-1] = '.'
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

def cycle(grid):
    slide_north(grid)
    slide_west(grid)
    slide_south(grid)
    slide_east(grid)

def main():
    # read in the grid
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line] for line in f])

    orig_grid = grid.copy()
    slide_north(grid)
    print('Part 1:', total_load(grid))

    grid = orig_grid.copy()
    seen = dict()
    loads = []
    for i in range(1000):
        cycle(grid)
        load = total_load(grid)
        loads.append(load)
        print(f'{i=} {load=}')
        k = ''.join(grid.flatten())
        if k in seen:
            cycle_len = i - seen[k]
            print(f'Found a cycle of length {cycle_len}')
            remaining = 1000000000 - i
            offset = remaining % cycle_len
            print(loads[i - cycle_len + offset] - 1)
            break
        else:
            seen[k] = i
        
main()
