import sys
import numpy as np
from collections import deque
from itertools import product

def neighbors(grid, row, col):
    deltas = [
        [0,1],
        [0,-1],
        [1,0],
        [-1,0],
    ]
        
    nrows, ncols = grid.shape
    for delta in deltas:
        r = row + delta[0]
        c = col + delta[1]
        if r >= 0 and r < nrows and c >= 0 and c < ncols and grid[r][c] == '.':
            yield(r, c)

def main():
    # read in the grid
    with open(sys.argv[1]) as f:
        grid = np.array([[ch for ch in line.rstrip()] for line in f])
            
    nrows, ncols = grid.shape
    max_steps = int(sys.argv[2])

    # find the starting position
    for row, col in product(range(nrows), range(ncols)):
        if grid[row][col] == 'S':
            start_pos = (row, col)
            grid[row][col] = '.'
            break

    seen = set()
    queue = deque()
    queue.append((0, start_pos[0], start_pos[1]))
    last_step = 0

    while True:
        step, row, col = queue.popleft()
        if step >= max_steps:
            break
        
        if step != last_step :
            seen.clear()
            last_step = step
            
        for r,c in neighbors(grid, row, col):
            if (r,c) not in seen:
                seen.add((r, c))
                queue.append((step+1, r, c))

    print('Part 1:', len(seen))

main()
