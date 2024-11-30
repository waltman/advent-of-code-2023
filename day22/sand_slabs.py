import sys
import numpy as np
from collections import defaultdict

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

    def can_drop(self, grid):
        return np.all(grid[self.y0:self.y1+1, self.x0:self.x1+1, self.z0-1] == 0)

    def drop(self, grid):
        grid[self.y0:self.y1+1,self.x0:self.x1+1,self.z0:self.z1+1] = 0
        self.z0 -= 1
        self.z1 -= 1
        grid[self.y0:self.y1+1,self.x0:self.x1+1,self.z0:self.z1+1] = self.name

    def below(self, grid):
        vals = set()
        if self.direction == 'x':
            for x in range(self.x0, self.x1+1):
                if (val := grid[self.y0, x, self.z0+1]) > 0:
                    vals.add(val)
        else:
            for y in range(self.y0, self.y1+1):
                if (val := grid[y, self.x0, self.z1+1]) > 0:
                    vals.add(val)

        return vals

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
            
    # construct the initial grid
    dimx = max(brick.x1 for brick in bricks) + 1
    dimy = max(brick.y1 for brick in bricks) + 1
    dimz = max(brick.z1 for brick in bricks) + 1

    grid = np.zeros([dimy, dimx, dimz], dtype=int)

    for brick in bricks:
        for z in range(brick.z0, brick.z1 + 1):
            grid[brick.y0:brick.y1+1,brick.x0:brick.x1+1,z] = brick.name

    grid[:,:,0] = -1

    # let the bricks drop
    order = sorted(bricks, key=lambda x: x.z0)
    done = False
    drop_pass = 0
    while not done:
        order = sorted(bricks, key=lambda x: x.z0)
        drop_pass += 1
        done = True
        for brick in order:
            while brick.can_drop(grid):
                brick.drop(grid)
                done = False
        
    safe = []
    recheck = []
    num_supports = defaultdict(int)
    for brick in bricks:
        below = brick.below(grid)
        if len(below) == 0:
            safe.append(brick.name)
        else:
            for b in below:
                num_supports[b] += 1
            recheck.append(brick)

    for brick in recheck:
        if all([num_supports[x] > 1 for x in brick.below(grid)]):
            safe.append(brick.name)
            
    print('Part 1', len(safe))

main()

