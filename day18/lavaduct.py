import sys
import numpy as np
from shapely import Polygon, Point
from random import random

# Many thanks to https://github.com/mmcclimon/advent-2023/blob/main/bin/day18.py
# for giving me some working code to base this one! He went with the triangle
# method instead of trapezoids, which looks like it was the way to go here.
def shoelace_triangle(points, perim):
    n = len(points)
    s1, s2 = 0, 0

    for i in range(n+1):
        j1 = i % n
        j2 = (i+1) % n
        s1 += points[j1][0] * points[j2][1]
        s2 += points[j1][1] * points[j2][0]

    return (perim + abs(s1-s2)) // 2 + 1

def decode_hex(hexcode):
    return "RDLU"[int(hexcode[-1])], int(hexcode[0:-1], 16)

def main():
    delta = {
        'R': np.array([0, 1]),
        'L': np.array([0, -1]),
        'D': np.array([1, 0]),
        'U': np.array([-1, 0]),
        }

    pos = np.array([0,0])
    pos2 = np.array([0,0])
    perim, perim2 = 0, 0
    points = [(0,0)]
    points2 = [(0,0)]
    with open(sys.argv[1]) as f:
        for line in f:
            toks = line.rstrip().split(' ')
            # part 1
            direct = toks[0]
            dist = int(toks[1])
            new_pos = pos + delta[direct] * dist
            perim += dist
            pos = new_pos
            points.append((pos[0], pos[1]))

            # part 2
            hexcode = toks[2][2:8]
            direct, dist = decode_hex(hexcode)
            new_pos = pos2 + delta[direct] * dist
            perim2 += dist
            pos2 = new_pos
            points2.append((pos2[0], pos2[1]))

    print('Part 1:', shoelace_triangle(points, perim))
    print('Part 2:', shoelace_triangle(points2, perim2))

main()
