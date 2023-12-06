from sys import argv
import re

# parse input
with open(argv[1]) as f:
    for line in f:
        m = re.match(r'(.*): (.*)', line.rstrip())
        if m.group(1) == 'Time':
            times = [int(d) for d in re.findall(r'\d+', m.group(2))]
        elif m.group(1) == 'Distance':
            dists = [int(d) for d in re.findall(r'\d+', m.group(2))]

part1 = 1

for i in range(len(times)):
    time = times[i]
    dist = dists[i]
    cnt = 0
    for j in range(1, time):
        travel = j * (time - j)
        if travel > dist:
            cnt += 1
    part1 *= cnt

print('Part 1:', part1)

time2 = int(''.join([str(d) for d in times]))
dist2 = int(''.join([str(d) for d in dists]))

part2 = 0
for i in range(1, time2):
    travel = i * (time2 - i)
    if travel > dist2:
        part2 += 1
    elif part2 > 0:
        break

print('Part 2:', part2)
