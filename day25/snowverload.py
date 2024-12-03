import sys
import networkx as nx
from itertools import combinations

def main():
    # parse the input and turn it into an undirected graph
    G = nx.Graph()

    with open(sys.argv[1]) as f:
        for line in f:
            toks1 = line.rstrip().split(': ')
            toks2 = toks1[1].split(' ')
            for x in toks2:
                G.add_edge(toks1[0], x)

    for e1, e2, e3 in combinations(G.edges, 3):
        G.remove_edge(e1[0], e1[1])
        G.remove_edge(e2[0], e2[1])
        G.remove_edge(e3[0], e3[1])
        if nx.number_connected_components(G) == 2:
            print(e1, e2, e3)
            prod = 1
            for cc in nx.connected_components(G):
                prod *= len(cc)
            print('Part 1:', prod)
            break
        else:
            G.add_edge(e1[0], e1[1])
            G.add_edge(e2[0], e2[1])
            G.add_edge(e3[0], e3[1])

main()
