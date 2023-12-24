import sys
import re
from collections import defaultdict

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

    return anonf, next_rule

def parse_rule(rule):
    if ':' in rule:
        return parse_cond(rule)
    else:
        anonf = lambda x: True
        return anonf, rule       

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

main()
