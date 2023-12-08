import sys
import re

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
