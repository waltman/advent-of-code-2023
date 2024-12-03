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

    # remove the 3 edges I found in the graphviz visualization

    # test.txt
    # G.remove_edge('hfx', 'pzl')
    # G.remove_edge('bvb', 'cmg')
    # G.remove_edge('nvd', 'jqt')

    # input.txt
    G.remove_edge('zhb', 'vxr')
    G.remove_edge('jbx', 'sml')
    G.remove_edge('vqj', 'szh')

    if nx.number_connected_components(G) == 2:
        prod = 1
        for cc in nx.connected_components(G):
            prod *= len(cc)
        print('Part 1:', prod)

main()
