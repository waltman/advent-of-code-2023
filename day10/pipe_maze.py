import sys
import numpy as np
from collections import deque

def start_pos(grid):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row][col] == 'S':
                return row, col

def adjacent(grid, row, col):
    deltas = {
        '|': [(-1,0), (+1,0)], # down, up
        '-': [(0,-1), (0,+1)], # left, right
        'F': [(0,+1), (+1,0)], # right, down
        'L': [(-1,0), (0,+1)], # up, right
        'J': [(-1,0), (0,-1)], # up, left
        '7': [(0,-1), (+1,0)], # left, down
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

# assume clockwise path
def find_adj(ch, row, col, new_row, new_col):
    drow, dcol = new_row - row, new_col - col
    if (drow, dcol) == (1, 0): # down
        inside = [(row, col-1)]
        outside = [(row, col+1)]
        if ch == '7':
            outside.append((row, col+1))
        elif ch == 'F':
            inside.append((row, col+1))
        elif ch != '|':
            print(f'unexpected {ch} while down')
    elif (drow, dcol) == (-1, 0): # up
        inside = [(row, col+1)]
        outside = [(row, col-1)]
        if ch == 'L':
            outside.append((row+1, col))
        elif ch == 'J':
            inside.append((row+1, col))
        elif ch != '|':
            print(f'unexpected {ch} while up')
    elif (drow, dcol) == (0, 1): # right
        inside = [(row+1, col)]
        outside = [(row-1, col)]
        if ch == 'F':
            outside.append((row-1, col))
        elif ch == 'L':
            inside.append((row-1, col))
        elif ch != '-':
            print(f'unexpected {ch} while right')
    else: # left
        inside = [(row-1, col)]
        outside = [(row+1, col)]
        if ch == 'J':
            outside.append((row+1, col))
        elif ch == '7':
            inside.append((row+1, col))
        elif ch != '-':
            print(f'unexpected {ch} while left')
    return inside, outside

def flood_fill(grid, walls, seeds):
    interior = seeds.copy()
    queue = deque(interior)
    while queue:
        row, col = queue.popleft()
        for r in range(row-1, -1, -1):
            if (r, col) in walls:
                break
            elif ((r,col)) not in interior:
                interior.add((r,col))
                queue.append((r,col))
        for r in range(row+1, grid.shape[0]):
            if (r, col) in walls:
                break
            elif ((r,col)) not in interior:
                interior.add((r, col))
                queue.append((r,col))
        for c in range(col-1, -1, -1):
            if (row, c) in walls:
                break
            elif ((row,c)) not in interior:
                interior.add((row, c))
                queue.append((row,c))
        for c in range(col+1, grid.shape[1]):
            if (row, c) in walls:
                break
            elif ((row,c)) not in interior:
                interior.add((row, c))
                queue.append((row,c))

    return interior

# broken attempt at solving part 2 with an even/odd algorithm
def even_odd(grid, walls):
    for row in range(grid.shape[0]):
        cnt = 0
        for col in range(grid.shape[1]):
            if (row, col) in walls:
                if col > 0 and (row, col-1) not in walls:
#                    print(f'crossing wall at ({row},{col})')
                    cnt += 1
            elif grid[row][col] == '.' and cnt % 2 == 1:
#                print((row, col))
                yield 1

def main():
    with open(sys.argv[1]) as f:
        grid = np.array([[c for c in line.rstrip()] for line in f])

    start_row, start_col = start_pos(grid)
    grid[start_row][start_col] = tile_type(grid, start_row, start_col)

    seen = {(start_row, start_col)}
    row, col = start_row, start_col
    done = False
    in_adjs = set()
    out_adjs = set()
    while not done:
        adjs = adjacent(grid, row, col)
        ok = False
        for adj in adjs:
            if adj in seen:
                continue
            else:
                new_row, new_col = adj
                seen.add(adj)
                ok = True

                in_adj, out_adj = find_adj(grid[row][col], row, col, new_row, new_col)
                in_adjs |= set(in_adj)
                out_adjs |= set(out_adj)
                row, col = new_row, new_col
                
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
    in_adjs -= seen
    out_adjs -= seen
    if len(in_adjs) < len(out_adjs): # guessed right!
        interior = flood_fill(grid, seen, in_adjs)
    else:
        interior = flood_fill(grid, seen, out_adjs)

    print('Part 2:', len(interior))
    print('Part 2 (even/odd) (broken):', sum(even_odd(grid, seen)))

main()

