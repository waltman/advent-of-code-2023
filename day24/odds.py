import sys

class Hailstone:
    def __init__(self, line):
        toks = line.split(' @ ')
        self.px, self.py, self.pz = (int(x) for x in toks[0].split(', '))
        self.vx, self.vy, self.vz = (int(x) for x in toks[1].split(', '))

    def __repr__(self):
        return f'({self.px}, {self.py}, {self.pz}) @ ({self.vx}, {self.vy}, {self.vz})'

def main():
    with open(sys.argv[1]) as f:
        hailstones = [Hailstone(line.rstrip()) for line in f]

    for stone in hailstones:
        print(stone)

main()
