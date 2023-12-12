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
    arrange = [c for c in condition]
    cnt = 0
    for prod in product('.#', repeat=len(idxs)):
        for i in range(len(idxs)):
            arrange[idxs[i]] = prod[i]
        if re.match(size_re, ''.join(arrange)):
#            print('match!', size_re, ''.join(arrange))
            cnt += 1

    return cnt

def main():
    part1 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            condition, sizes = line.rstrip().split(' ')
            size_re = size_regexp(sizes)
            part1 += matches(condition, size_re)

    print('Part 1:', part1)

main()
