#!/usr/bin/env python3

def decode(s):
    s = s.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
    return int(s, 2) # uid 

def rowseat(uid):
    return (uid >> 3), (uid & 0x0008) # row, seat, uid

codes = [line.rstrip() for line in open("./input")]
uids = sorted([uid for uid in [decode(code) for code in codes]])
print(f"Highest ID = {uids[-1]}")

missing = set(range(0, 1024)) - set(uids)
print(missing)
