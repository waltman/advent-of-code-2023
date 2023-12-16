import sys
import numpy as np

def score(pattern):
    print(f'shape = {pattern.shape}')
    nrows, ncols = pattern.shape
    
    # test rows
    for r in range(nrows - 1):
        print('row =', r)
        if np.all(pattern[r,:] == pattern[r+1,:]):
            ok = True
            print(f'checking at row {r}')
            for i in range(1, r+1):
                r0, r1 = r-i, r+i+1
                if r0 < 0 or r1 >= nrows:
                    break
                print(f'checking rows ({r0},{r1})')
                if np.any(pattern[r0,:] != pattern[r1,:]):
                    ok = False
                    print('false match at', r)
                    break
            if ok:
                print('found a row match at', r)
                return (r+1) * 100

    # test columns
    for c in range(ncols - 1):
        print('col =', c)
        if np.all(pattern[:,c] == pattern[:,c+1]):
            ok = True
            print(f'checking at col {c}')
            for i in range(1, c+1):
                c0, c1 = c-i, c+i+1
                if c0 < 0 or c1 >= ncols:
                    break
                print(f'checking cols ({c0},{c1})')
                if np.any(pattern[:,c0] != pattern[:,c1]):
                    ok = False
                    print('false match at', c)
                    break
            if ok:
                print('found a column match at', c)
                return c+1

    print('no reflection!')
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
