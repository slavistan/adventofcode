#!/usr/bin/env python3

import networkx as nx

g = nx.DiGraph()
for bag, _, content in [line.rstrip(".\n").partition(" contain ") for line in open("./input")]:
    bag = bag.replace(" bags", "").replace(" ", "")
    g.add_node(bag)
    content = content.replace("no other bags", "")
    for seg in [s.split(" ") for s in content.split(", ") if len(s) != 0]:
        count = int(seg[0])
        subbag = seg[1] + seg[2]
        g.add_edge(bag, subbag, weight=count)

def count_subbags(g, source):
    total = 0
    for nbr in g.neighbors(source):
        total += g[source][nbr]["weight"] * (1 + count_subbags(g, nbr))
    return total

print("Part 1: ", len(nx.ancestors(g, "shinygold")), sep="")
print("Part 2: ", count_subbags(g, "shinygold"), sep="")
