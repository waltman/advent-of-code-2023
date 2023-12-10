import sys
import numpy as np

def start_pos(grid):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row][col] == 'S':
                return row, col

def adjacent(grid, row, col):
    deltas = {
        '|': [(-1,0), (+1,0)],
        '-': [(0,-1), (0,+1)],
        'F': [(0,+1), (+1,0)],
        'L': [(-1,0), (0,+1)],
        'J': [(-1,0), (0,-1)],
        '7': [(0,-1), (+1,0)],
    }

    d1, d2 = deltas[grid[row][col]]
    return [(row+d1[0], col+d1[1]), (row+d2[0], col+d2[1])]

# determine tile type based on neighbors
def tile_type(grid, row, col):
    tile = {
        'ns': '|',
        'we': '-',
        'ne': 'L',
        'nw': 'J',
        'se': 'F',
        'sw': '7',
    }

    neighbors = []

    if row > 0 and grid[row-1][col] in '|F7':
        neighbors.append('n')
    if row+1 < grid.shape[0] and grid[row+1][col] in '|LJ':
        neighbors.append('s')
    if col > 0 and grid[row][col-1] in '-FL':
        neighbors.append('w')
    if col+1 < grid.shape[1] and grid[row][col+1] in '-7J':
        neighbors.append('e')

    return tile[''.join(neighbors)]

def main():
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])

    start_row, start_col = start_pos(grid)
    grid[start_row][start_col] = tile_type(grid, start_row, start_col)

    seen = {(start_row, start_col)}
    row, col = start_row, start_col
    done = False
    while not done:
        adjs = adjacent(grid, row, col)
        ok = False
        for adj in adjs:
            if adj in seen:
                continue
            else:
                row, col = adj
                seen.add(adj)
                ok = True
                break
        if not ok:
            # hopefully we're back at the start
            for adj in adjs:
                if adj == (start_row, start_col):
                    done = True
                    break
                          
            if not done:
                print("OOPS!", adjs)
                done = True

    print('Part 1:', len(seen) // 2)

main()

