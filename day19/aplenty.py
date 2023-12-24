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
        anonf = lambda xmas: xmax[cat] > val

    return anonf, next_rule

def parse_rule(rule):
    if ':' in rule:
        return rule.split(':')
    else:
        anonf = lambda x: True
        return anonf, rule       

def main():
    workflow = defaultdict(list)
    parts = []

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

    print(parts)
main()
