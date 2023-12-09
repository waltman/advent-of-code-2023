import sys

def next_val(report):
    seqs = [report]
    while any(seqs[-1]):
        seqs.append([seqs[-1][i+1] - seqs[-1][i] for i in range(len(seqs[-1])-1)])

    delta = 0
    for i in range(len(seqs)-2, -1, -1):
        delta = seqs[i][-1] + delta

    return delta

def prev_val(report):
    seqs = [report]
    while any(seqs[-1]):
        seqs.append([seqs[-1][i+1] - seqs[-1][i] for i in range(len(seqs[-1])-1)])

    delta = 0
    for i in range(len(seqs)-2, -1, -1):
        delta = seqs[i][0] - delta

    return delta

def main():
    with open(sys.argv[1]) as f:
        reports = [[int(d) for d in line.split()] for line in f]

    for report in reports:
        next_val(report)

    print('Part 1:', sum([next_val(report) for report in reports]))
    print('Part 2:', sum([prev_val(report) for report in reports]))

main()
