import sys
import numpy as np
from collections import deque

def neighbors(grid, row, col, direct, score):
    delta = {
        'r': [0,1],
        'l': [0,-1],
        'd': [1,0],
        'u': [-1,0],
    }
    next_dir = {
        'r': ['u', 'd'],
        'l': ['u', 'd'],
        'u': ['l', 'r'],
        'd': ['l', 'r'],
    }
        
    nrows, ncols = grid.shape
    for _ in range(3):
        row += delta[direct][0]
        col += delta[direct][1]
        if row >= 0 and row < nrows and col >= 0 and col < ncols:
            score += grid[row][col]
            yield(row, col, score, next_dir[direct][0])
            yield(row, col, score, next_dir[direct][1])
        else:
            break

def main():
    # read in the grid
    with open(sys.argv[1]) as f:
        grid = np.array([[int(d) for d in line.rstrip()] for line in f])
            
    nrows, ncols = grid.shape
    max_score = grid.shape[0] * grid.shape[1] * 9
    best_score = max_score
    seen = dict()
    queue = deque()
    for row, col, score, direct in neighbors(grid, 0, 0, 'r', 0):
        queue.append((row, col, score, direct))

    while queue:
        row, col, score, direct = queue.popleft()

        # did we read the goal?
        if row == nrows-1 and col == ncols-1:
            if score < best_score:
                print('New best score of', score)
                best_score = score

        # is it impossible to beat the best score?
        elif score >= best_score:
            continue

        # have we already been here
        elif score < seen.get((row, col, direct), best_score):
            seen[(row, col, direct)] = score
            for row, col, score, direct in neighbors(grid, row, col, direct, score):
                queue.append((row, col, score, direct))

    print('Part 1', best_score)
    
main()
