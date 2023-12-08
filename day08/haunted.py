import sys
import re
from math import lcm

def part2_steps(k, mapping, lr):
    idx = 0
    steps = 0
    while k[-1] != 'Z':
        i = 0 if lr[idx] == 'L' else 1
        k = mapping[k][i]
        steps += 1
        idx = (idx + 1) % len(lr)
    return steps

def main():
    mapping = dict()
    with open(sys.argv[1]) as f:
        lr = f.readline().rstrip()
        f.readline()
        for line in f:
            m = re.match(r'(.*) = \((.*), (.*)\)', line.rstrip())
            k = m.group(1)
            left = m.group(2)
            right = m.group(3)
            mapping[k] = (left, right)

    part1 = 0
    idx1 = 0
    k = 'AAA'
    while k != 'ZZZ' :
        i = 0 if lr[idx1] == 'L' else 1
        k = mapping[k][i]
        part1 += 1
        idx1 = (idx1 + 1) % len(lr)

    print('Part 1:', part1)

    k2 = [k for k in mapping.keys() if k[-1] == 'A']
    
    steps = [part2_steps(k, mapping, lr) for k in k2]
    print('Part 2:', lcm(*steps))
    
main()
