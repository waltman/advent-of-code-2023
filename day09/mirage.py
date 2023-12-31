import sys

def extrapolate(report):
    seqs = [report]
    while any(seqs[-1]):
        seqs.append([seqs[-1][i+1] - seqs[-1][i] for i in range(len(seqs[-1])-1)])

    return seqs

def next_val(report):
    seqs = extrapolate(report)
    delta = 0
    for i in range(len(seqs)-2, -1, -1):
        delta = seqs[i][-1] + delta

    return delta

def prev_val(report):
    seqs = extrapolate(report)
    delta = 0
    for i in range(len(seqs)-2, -1, -1):
        delta = seqs[i][0] - delta

    return delta

def main():
    with open(sys.argv[1]) as f:
        reports = [list(map(int, line.split())) for line in f]

    print('Part 1:', sum(map(next_val, reports)))
    print('Part 2:', sum(map(prev_val, reports)))

main()
