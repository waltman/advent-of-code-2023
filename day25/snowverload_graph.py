import sys
import networkx as nx
from itertools import combinations

def main():
    # generate graphviz code for the input
    print("graph G {")

    with open(sys.argv[1]) as f:
        for line in f:
            toks1 = line.rstrip().split(': ')
            toks2 = toks1[1].split(' ')
            print(f'{toks1[0]} -- {{ {' '.join(toks2)} }}')
    print('}')

main()
