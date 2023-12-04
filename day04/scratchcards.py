from sys import argv
import re

part1 = 0
card_cnt = dict()
with open(argv[1]) as f:
    for line in f:
        card, data = line.rstrip().split(': ')
        card_num = int(re.search(r'(\d+)', card).group(1))
        card_cnt.setdefault(card_num, 1)
        them, us = data.split(' | ')
        them_set = {int(d) for d in re.findall(r'\d+', them)}
        us_set = {int(d) for d in re.findall(r'\d+', us)}
        common = them_set & us_set
        if cnt := len(common):
            part1 += 2 ** (cnt-1)
            for i in range(card_num+1, card_num+cnt+1):
                card_cnt[i] = card_cnt.get(i, 1) + card_cnt[card_num]

print('Part 1:', part1)
print('Part 2:', sum([card_cnt[i] for i in range(1, card_num+1)]))
