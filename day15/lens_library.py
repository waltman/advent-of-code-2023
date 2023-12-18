import sys
import re
from collections import defaultdict

def HASH(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val

def add_lens(box, label, lens_val):
    boxnum = HASH(label)
    for i in range(len(box[boxnum])):
        if box[boxnum][i][0] == label:
            box[boxnum][i] = (label, lens_val)
            return
    box[boxnum].append((label, lens_val))

def delete_lens(box, label):
    boxnum = HASH(label)
    for i in range(len(box[boxnum])):
        if box[boxnum][i][0] == label:
            box[boxnum].pop(i)
            return

def focusing_power(boxnum, lenses):
    return sum([(boxnum+1) * (i+1) * lenses[i][1] for i in range(len(lenses))])

def main():
    with open(sys.argv[1]) as f:
        steps = f.read().rstrip().split(',')

    print('Part 1:', sum([HASH(step) for step in steps]))

    box = defaultdict(list)
    for step_str in steps:
        m = re.match(r'^([a-z]+)(.*)$', step_str)
        label = m.group(1)
        if m.group(2)[0] == '=':
            lens_val = int(m.group(2)[1:])
            add_lens(box, label, lens_val)
        else:
            delete_lens(box, label)

    print('Part 2:', sum([focusing_power(k,v) for k,v in box.items()]))

main()
