#!/usr/bin/env python3

def sum_distinct(numbers, num):
    for ii in range(len(numbers)):
        for jj in range(ii + 1, len(numbers)):
            if num == numbers[ii] + numbers[jj] and numbers[ii] != numbers[jj]:
                return (ii, jj, numbers[ii], numbers[jj])
    return None

def contiguous_sum(numbers, num):
    for ii in range(len(numbers)):
        total = numbers[ii]
        for jj in range(ii + 1, len(numbers)):
            total = total + numbers[jj]
            if total > num:
                break
            elif total == num:
                return ii, jj

def gogogo(cypher, lenpreamble):
    for ii in range(lenpreamble, len(cypher)):
        split = sum_distinct(cypher[ii - lenpreamble: ii], cypher[ii]);
        if split is None:
            return cypher[ii]
    return None

cypher = [int(line.rstrip()) for line in open("./input")]
lenpreamble = 25

nonsum = gogogo(cypher, lenpreamble)
print(nonsum)

contsum = contiguous_sum(cypher, nonsum)
small = min(cypher[contsum[0]:contsum[1]+1])
large = max(cypher[contsum[0]:contsum[1]+1])
print(f"{small} + {large} = {small + large}")
