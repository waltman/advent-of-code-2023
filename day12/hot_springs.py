import sys
import re
from itertools import product
from functools import cache

def size_regexp(sizes_str):
    sizes = ['#{' + str(d) + '}' for d in sizes_str.split(',')]
    return r'^\.*' + '\\.+'.join(sizes) + r'\.*$'

def qm_pos(s):
    return [i for i in range(len(s)) if s[i] == '?']

def matches(condition, size_re):
    idxs = qm_pos(condition)
#    print('in matches, len =', len(idxs))
    arrange = [c for c in condition]
    cnt = 0
    for prod in product('.#', repeat=len(idxs)):
        for i in range(len(idxs)):
            arrange[idxs[i]] = prod[i]
        if re.match(size_re, ''.join(arrange)):
            cnt += 1

    return cnt

def fact(n):
    prod = 1
    for x in range(2, n+1):
        prod *= x
    return prod

def choose(n, k):
    return fact(n) / (fact(k) * fact(n-k))

# I was stumped on part 2 nd I borrowed this code from
# https://advent-of-code.xavd.id/writeups/2023/day/12/
@cache
def num_valid_solutions(record: str, groups: tuple[int, ...]) -> int:
    if not record:
        # if there are no more spots to check;
        # our only chance at success is if there are no `groups` left
        return len(groups) == 0

    if not groups:
        # if there are no more groups the only possibility of success
        # is that there are no `#` remaining
        return "#" not in record

    char, rest_of_record = record[0], record[1:]

    if char == ".":
        # dots are ignores, so keep recursing
        return num_valid_solutions(rest_of_record, groups)

    if char == "#":
        group = groups[0]
        # we're at the start of a group! make sure there are enough here to fill the first group
        # to be valid, we have to be:
        if (
            # long enough to match
            len(record) >= group
            # made of only things that can be `#` (no `.`)
            and all(c != "." for c in record[:group])
            # either at the end of the record (allowed)
            # or the next character isn't also a `#` (would be too big)
            and (len(record) == group or record[group] != "#")
        ):
            return num_valid_solutions(record[group + 1 :], groups[1:])

        return 0

    if char == "?":
        return num_valid_solutions(f"#{rest_of_record}", groups) + num_valid_solutions(
            f".{rest_of_record}", groups
        )

def main():
    part1 = 0
    part2 = 0
    lineno = 1
    with open(sys.argv[1]) as f:
        for line in f:
            lineno += 1
            condition, sizes = line.rstrip().split(' ')
            size_re = size_regexp(sizes)
            part1 += matches(condition, size_re)
            sizes2 = ','.join([str(d) for d in [int(d) for d in sizes.split(',')] * 5])
            sizes2_re = size_regexp(sizes2)
            condition2 = '?'.join([condition]*5)
            sizes2a = tuple([int(d) for d in sizes.split(',')] * 5)
            # qs = sum([1 for c in condition2 if c == '?'])
            # ps = sum([1 for c in condition2 if c == '#'])
            # tot = sum([int(d) for d in sizes2.split(',')])
            # left = tot - ps
            # print(condition2, sizes, sizes2, sizes2_re)
            # print(qs, ps, tot, left, choose(qs, left))
#            part2 += matches(condition2, sizes2_re)
            part2 += num_valid_solutions(condition2, sizes2a)

    print('Part 1:', part1)
    print('Part 2:', part2)

main()
