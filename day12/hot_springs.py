import sys
import re
from itertools import product

def size_regexp(sizes_str):
    sizes = ['#{' + str(d) + '}' for d in sizes_str.split(',')]
    return r'^\.*' + '\\.+'.join(sizes) + r'\.*$'

def qm_pos(s):
    return [i for i in range(len(s)) if s[i] == '?']

def matches(condition, size_re):
    idxs = qm_pos(condition)
    print('in matches, len =', len(idxs))
    arrange = [c for c in condition]
    cnt = 0
    for prod in product('.#', repeat=len(idxs)):
        for i in range(len(idxs)):
            arrange[idxs[i]] = prod[i]
        if re.match(size_re, ''.join(arrange)):
            cnt += 1

    return cnt

def main():
    part1 = 0
    part2 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            condition, sizes = line.rstrip().split(' ')
            size_re = size_regexp(sizes)
            part1 += matches(condition, size_re)
            sizes2 = ','.join([str(d) for d in [int(d) for d in sizes.split(',')] * 5])
            sizes2_re = size_regexp(sizes2)
            condition2 = '?'.join([condition]*5)
            print(condition2, sizes, sizes2, sizes2_re)
            part2 += matches(condition2, sizes2_re)

    print('Part 1:', part1)
    print('Part 2:', part2)

main()
