import sys
from itertools import combinations
import numpy as np

class Hailstone:
    def __init__(self, line):
        toks = line.split(' @ ')
        self.px, self.py, self.pz = (int(x) for x in toks[0].split(', '))
        self.vx, self.vy, self.vz = (int(x) for x in toks[1].split(', '))

    def slope2(self):
        return self.vy / self.vx

    def eqn2(self):
        m = self.slope2()
        return m, -1, (self.py - m * self.px)

    def __repr__(self):
        return f'({self.px}, {self.py}, {self.pz}) @ ({self.vx}, {self.vy}, {self.vz})'

def intersect2(s1, s2):
    a1, b1, c1 = s1.eqn2()
    a2, b2, c2 = s2.eqn2()
    denom = a1*b2 - a2*b1
    if denom == 0:
        return None, None, False
    else:
        x = (b1*c2 - b2*c1) / denom
        y = (c1*a2 - c2*a1) / denom
        reachablex1 = (x >= s1.px and s1.vx > 0) or (x <= s1.px and s1.vx < 0)
        reachabley1 = (y >= s1.py and s1.vy > 0) or (y <= s1.py and s1.vy < 0)
        reachablex2 = (x >= s2.px and s2.vx > 0) or (x <= s2.px and s2.vx < 0)
        reachabley2 = (y >= s2.py and s2.vy > 0) or (y <= s2.py and s2.vy < 0)
        return x, y, reachablex1 and reachabley1 and reachablex2 and reachabley2 

def main():
    with open(sys.argv[1]) as f:
        hailstones = [Hailstone(line.rstrip()) for line in f]

    lower = int(sys.argv[2])
    upper = int(sys.argv[3])

    cnt = 0
    for s1, s2 in combinations(hailstones, 2):
        x, y, reachable = intersect2(s1, s2)
        if x and lower <= x <= upper and lower <= y <= upper and reachable:
            cnt += 1
    print('Part 1:', cnt)

    # linear albegra solution from https://www.reddit.com/r/adventofcode/comments/18pnycy/2023_day_24_solutions
    pos0 = np.array([hailstones[0].px, hailstones[0].py, hailstones[0].pz], dtype=np.float128)
    pos1 = np.array([hailstones[1].px, hailstones[1].py, hailstones[1].pz], dtype=np.float128)
    pos2 = np.array([hailstones[2].px, hailstones[2].py, hailstones[2].pz], dtype=np.float128)
    vel0 = np.array([hailstones[0].vx, hailstones[0].vy, hailstones[0].vz], dtype=np.float128)
    vel1 = np.array([hailstones[1].vx, hailstones[1].vy, hailstones[1].vz], dtype=np.float128)
    vel2 = np.array([hailstones[2].vx, hailstones[2].vy, hailstones[2].vz], dtype=np.float128)

    p1 = pos1 - pos0
    v1 = vel1 - vel0
    p2 = pos2 - pos0
    v2 = vel2 - vel0
    t1 = -np.dot(np.cross(p1, p2), v2) / np.dot(np.cross(v1, p2), v2)
    t2 = -np.dot(np.cross(p1, p2), v1) / np.dot(np.cross(p1, v2), v1)
    print(f'{t1=}, {t2=}')

    c1 = pos1 + t1*vel1
    c2 = pos2 + t2*vel2

    v = (c2 - c1) / (t2 - t1)
    p = c1 - t1 * v

    print(p, v)
    print('Part 2:', np.sum(p))
    print(p[0] + p[1] + p[2])

main()
