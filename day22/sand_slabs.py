import sys
import numpy as np

class Brick:
    def __init__(self, name, p0, p1):
        self.name = name
        self.x0 = p0[0]
        self.y0 = p0[1]
        self.z0 = p0[2]
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.z1 = p1[2]

        assert self.x0 <= self.x1
        assert self.y0 <= self.y1
        assert self.z0 <= self.z1

        if self.x0 != self.x1:
            self.direction = 'x'
        elif self.y0 != self.y1:
            self.direction = 'y'
        else:
            self.direction = 'z'

    def __repr__(self):
        return f'{self.name}: ({self.x0}, {self.y0}, {self.z0}), ({self.x1}, {self.y1}, {self.z1}) {self.direction}'

def main():
    bricks = []

    # parse the input
    with open(sys.argv[1]) as f:
        cnt = 1
        for line in f:
            ends = line.rstrip().split('~')
            p0 = [int(x) for x in ends[0].split(',')]
            p1 = [int(x) for x in ends[1].split(',')]
            bricks.append(Brick(cnt, p0, p1))
            cnt += 1
            
    for brick in bricks:
        print(brick)
main()

