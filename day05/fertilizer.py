from sys import argv

with open(argv[1]) as f:
    for line in f:
        if line.startswith('seeds: '):
            seeds = [int(d) for d in line[7:].split(' ')]
            print(seeds)
