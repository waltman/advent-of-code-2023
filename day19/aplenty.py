import sys
import re
from collections import defaultdict
import copy

def parse_cond(cond):
    m = re.match(r'^(.*)([<>])(.*):(.*)$', cond)
    cat = m.group(1)
    op = m.group(2)
    val = int(m.group(3))
    next_rule = m.group(4)

    if op == '<':
        anonf = lambda xmas: xmas[cat] < val
    else:
        anonf = lambda xmas: xmas[cat] > val

    return anonf, next_rule, cat, op, val

def parse_rule(rule):
    if ':' in rule:
        return parse_cond(rule)
    else:
        anonf = lambda x: True
        return anonf, rule, (rule), None, None

# split up vals to those for which the condition is true vs false
def split_set(vals, op, n):
    if op is None:
        return vals, None
    
    if op == '<':
        mask = set(range(1, n))
    else:
        mask = set(range(n+1, 4001))
    out_set = vals - mask
    return vals - out_set, out_set

def all_possible(workflow):
    ranges = {
        'x': set(range(1,4001)),
        'm': set(range(1,4001)),
        'a': set(range(1,4001)),
        's': set(range(1,4001)),
    }
    total = 0
    stack = [('in', ranges)]
    seen = set()
    while stack:
        rule, ranges = stack.pop()

        if rule in seen:
            print('seen rule', rule)
            continue

        if rule == 'R':
            continue

        if rule == 'A':
            prod = len(ranges['x']) * len(ranges['m']) * len(ranges['a']) * len(ranges['s'])
            total += prod
            continue

        seen.add(rule)

        for cond in workflow[rule]:
            next_rule, cat, op, val = cond[1:5]
            if op is None:
                stack.append((next_rule, copy.deepcopy(ranges)))
            else:
                in_set, out_set = split_set(ranges[cat], op, val)
                new_ranges = copy.deepcopy(ranges)
                new_ranges[cat] = in_set.copy()
                stack.append((next_rule, new_ranges))
                ranges[cat] = out_set.copy()

    return total
    
def main():
    workflow = defaultdict(list)
    parts = []
    part1 = 0

    with open(sys.argv[1]) as f:
        for line in f:
            if 'a' <= line[0] <= 'z': # workflow
                m = re.match(r'^(.*)\{(.*)\}', line.rstrip())
                for rule in m.group(2).split(','):
                    workflow[m.group(1)].append(parse_rule(rule))
            elif line[0] == '{': # parts
                toks1 = line[1:-2].split(',')
                xmas = {}
                for tok1 in toks1:
                    toks2 = tok1.split('=')
                    xmas[toks2[0]] = int(toks2[1])
                parts.append(xmas)

    for part in parts:
        rule = 'in'
        while rule not in {'A', 'R'}:
            for cond in workflow[rule]:
                if cond[0](part):
                    rule = cond[1]
                    break

        if rule == 'A':
            part1 += sum(part.values())

    print('Part 1:', part1)
    print('Part 2:', all_possible(workflow))

main()
