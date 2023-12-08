import sys
import re

def done(keys):
    return all([k[-1] == 'Z' for k in keys])

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
    part2 = 0
    idx = 0
    while not done(k2):
        i = 0 if lr[idx] == 'L' else 1
        k2 = [mapping[k][i] for k in k2]
        part2 += 1
        idx = (idx + 1) % len(lr)
#        print(idx, part2, k2)

    print('Part 2:', part2)

main()
