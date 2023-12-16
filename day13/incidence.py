import sys
import numpy as np

def score(pattern):
    nrows, ncols = pattern.shape
    
    # test rows
    for r in range(nrows - 1):
        if np.all(pattern[r,:] == pattern[r+1,:]):
            ok = True
            for i in range(1, r+1):
                r0, r1 = r-i, r+i+1
                if r0 < 0 or r1 >= nrows:
                    break
                if np.any(pattern[r0,:] != pattern[r1,:]):
                    ok = False
                    break
            if ok:
                return (r+1) * 100

    # test columns
    for c in range(ncols - 1):
        if np.all(pattern[:,c] == pattern[:,c+1]):
            ok = True
            for i in range(1, c+1):
                c0, c1 = c-i, c+i+1
                if c0 < 0 or c1 >= ncols:
                    break
                if np.any(pattern[:,c0] != pattern[:,c1]):
                    ok = False
                    break
            if ok:
                return c+1

    return 0

def main():
    # parse the input
    patterns = []
    lines = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.rstrip()
            if line:
                lines.append([c for c in line])
            else:
                patterns.append(np.array(lines))
                lines = []

    if lines:
        patterns.append(np.array(lines))

    print('Part 1:', sum(map(score, patterns)))

main()
