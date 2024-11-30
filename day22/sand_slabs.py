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

    def can_drop(self, grid):
        return np.all(grid[self.x0:self.x1+1, self.y0:self.y1+1, self.z0-1] == 0)

    def drop(self, grid):
        grid[self.x0:self.x1+1,self.y0:self.y1+1,self.z0:self.z1+1] = 0
        self.z0 -= 1
        self.z1 -= 1
        grid[self.x0:self.x1+1,self.y0:self.y1+1,self.z0:self.z1+1] = self.name

    def above(self, grid):
        vals = set()
        if self.direction == 'x':
            for x in range(self.x0, self.x1+1):
                if (val := grid[x, self.y0, self.z0-1]) > 0:
                    vals.add(val)
        else:
            for y in range(self.y0, self.y1+1):
                if (val := grid[self.x0, y, self.z0-1]) > 0:
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

    grid = np.zeros([dimx, dimy, dimz], dtype=int)

    for brick in bricks:
        for z in range(brick.z0, brick.z1 + 1):
            grid[brick.x0:brick.x1+1,brick.y0:brick.y1+1,z] = brick.name

    grid[:,:,0] = -1

    for z in range(dimz):
        print(z)
        print(grid[:,:,z])


    # let the bricks drop
    order = sorted(bricks, key=lambda x: x.z0)
    print([x.name for x in order])
    done = False
    while not done:
        done = True
        for brick in order:
            while brick.can_drop(grid):
                brick.drop(grid)
                done = False
        
    print('after')
    for z in range(dimz):
        print(z)
        print(grid[:,:,z])
    
    safe = set()
    unused = {brick.name for brick in bricks}
    for brick in bricks:
        above = brick.above(grid)
        print(brick.name, above)
        unused -= above
        if len(above) > 1:
            print(f'{above=}')
            safe |= above
        
    print(f'{safe=}, {unused=}')
    print('Part1:', len(safe) + len(unused))
    print(len(safe), len(unused))
    print(safe & unused)

main()

