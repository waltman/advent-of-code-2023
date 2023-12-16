import sys
import numpy as np

def score(pattern):
    # test rows
    for r in range(pattern.shape[0] - 1):
        print(r)
        if np.all(pattern[r,:] == pattern[r+1,:]):
            ok = True
            print(f'checking at row {r}')
            for i in range(min(r, pattern.shape[0]-r-1)):
                print(f'checking ({r-i},{r+i+1})')
                if np.any(pattern[r-i,:] != pattern[r+i+1,:]):
                    ok = False
                    print('false match at', r)
                    break
            if ok:
                print('found a row match at', r)
                return (r+1) * 100

    # test columns
    for c in range(pattern.shape[1] - 1):
        print(c)
        if np.all(pattern[:,c] == pattern[:,c+1]):
            ok = True
            print(f'checking at column {c}')
            for i in range(min(c, pattern.shape[1]-c-1)):
                print(f'checking ({c-i},{c+i+1})')
                if np.any(pattern[:,c-i] != pattern[:,c+i+1]):
                    ok = False
                    print('false column match at', c)
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
