from sys import argv
import re

part1 = 0
with open(argv[1]) as f:
    for line in f:
        card, data = line.rstrip().split(': ')
        them, us = data.split(' | ')
        them_set = {int(d) for d in re.findall(r'\d+', them)}
        us_set = {int(d) for d in re.findall(r'\d+', us)}
        common = them_set & us_set
        if cnt := len(common):
            part1 += 2 ** (cnt-1)

print('Part 1:', part1)
