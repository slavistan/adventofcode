#!/usr/bin/env python3
from functools import reduce

intersecttotal = 0
uniontotal = 0
for group in open("./input").read().split("\n\n"):
    groupans = []
    for member in [m.rstrip() for m in group.split("\n") if len(m.rstrip()) != 0]:
        groupans.append(set(member))
    intersect = reduce(lambda x, y: x.intersection(y), groupans, groupans[0])
    union = reduce(lambda x, y: x.union(y), groupans, groupans[0])
    intersecttotal = intersecttotal + len(intersect)
    uniontotal = uniontotal + len(union)

print(f"Part 1: total = {uniontotal}")
print(f"Part 2: total = {intersecttotal}")
