import sys
import numpy as np
from shapely import Polygon, Point

def main():
    delta = {
        'R': np.array([0, 1]),
        'L': np.array([0, -1]),
        'D': np.array([1, 0]),
        'U': np.array([-1, 0]),
        }

    lines = []
    pos = np.array([0,0])
    meters = 0
    min_row = max_row = min_col = max_col = 0
    vedge = set()
    hedge = set()
    points = [(0,0)]
    with open(sys.argv[1]) as f:
        for line in f:
            toks = line.rstrip().split(' ')
            direct = toks[0]
            dist = int(toks[1])
            new_pos = pos + delta[direct] * dist
            lines.append((tuple(pos), tuple(new_pos)))
            meters += dist
            min_row = min(min_row, new_pos[0])
            max_row = max(max_row, new_pos[0])
            min_col = min(min_col, new_pos[1])
            max_col = max(max_col, new_pos[1])
            for i in range(dist):
                if direct in {'U','D'}:
                    vedge.add((pos[0] + delta[direct][0] * i, pos[1] + delta[direct][1] * i))
                else:
                    hedge.add((pos[0] + delta[direct][0] * i, pos[1] + delta[direct][1] * i))
            pos = new_pos
            points.append((pos[0], pos[1]))

    polygon = Polygon(points)
    for row in range(min_row, max_row+1):
        for col in range(min_col, max_col+1):
            if polygon.contains(Point((row, col))):
                meters += 1

    print('Part 1:', meters)

main()
