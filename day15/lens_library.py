import sys

def HASH(s):
    val = 0
    for c in s:
        val = ((val + ord(c)) * 17) % 256
    return val

def main():
    with open(sys.argv[1]) as f:
        steps = f.read().rstrip().split(',')

        print('Part 1:', sum([HASH(step) for step in steps]))

main()
