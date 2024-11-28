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
            
    # construct the initial grid
    dimx = max(brick.x1 for brick in bricks) + 1
    dimy = max(brick.y1 for brick in bricks) + 1
    dimz = max(brick.z1 for brick in bricks) + 1

    grid = np.zeros([dimx, dimy, dimz], dtype=np.int32)

    for brick in bricks:
        for z in range(brick.z0, brick.z1 + 1):
            grid[brick.x0:brick.x1+1,brick.y0:brick.y1+1,z] = brick.name

    for z in range(dimz):
        print(z)
        print(grid[:,:,z])


    # let the bricks drop
    order = sorted(bricks, key=lambda x: x.z0)
    print([x.name for x in order])
    # done = False
    # while not done:
    #     done = True
        
    
main()

