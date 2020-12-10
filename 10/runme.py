#!/usr/bin/env python3

from functools import reduce

jolts = [int(l.rstrip()) for l in open("./input")]
jolts.append(0)
jolts.append(max(jolts) + 3)
jolts.sort()

adjdiffs = []
prevjolt = jolts[0]
for ii in range(1, len(jolts)):
    diff = jolts[ii] - prevjolt
    adjdiffs.append(diff)
    prevjolt = jolts[ii]

print(adjdiffs.count(1) * adjdiffs.count(3))

# p2

lut = [0, 1, 1, 2]
for ii in range(len(lut), 20):
    lut.append(lut[ii-1] + lut[ii-2] + lut[ii-3])

where3 = [ii for ii in range(len(adjdiffs)) if adjdiffs[ii] == 3]
lowerii = 0
lenseg = []
for ii in range(len(where3)):
    lenseg.append(where3[ii]-lowerii+1)
    lowerii = where3[ii]+1

print(reduce(lambda x, y: x * lut[y], lenseg, 1))
