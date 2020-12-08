#!/usr/bin/env python3

from itertools import repeat
from copy import deepcopy

def parse_instructions(infile): # opcode, arg
    instructions = []
    for l in [line.rstrip() for line in open(infile)]:
        instr, param = l.split(" ")
        param = int(param)
        instructions.append([instr, param])
    return instructions

def run(instructions): # True/False (terminated properly), acc
    ip = 0
    acc = 0
    instr_n = list(repeat(0, len(instructions)))
    while True:
        if (ip == len(instructions)): # proper finish
            return 0, acc
        if (ip > len(instructions) or ip < 0): # crash
            return 1, acc
        if (instr_n[ip] > 0): # infinite loop
            return 2, acc
        instr_n[ip] = instr_n[ip] + 1
        if instructions[ip][0] == "nop":
            ip = ip + 1
            continue
        elif instructions[ip][0] == "acc":
            acc = acc + instructions[ip][1]
            ip = ip + 1
            continue
        elif instructions[ip][0] == "jmp":
            ip = ip + instructions[ip][1]
            continue
        else:
            return 1, acc

instr = parse_instructions("./input")

print(f"Part 1: acc = '{run(instr)[1]}'")

nops_at = [ii for ii in range(len(instr)) if instr[ii][0] == "nop"]
jmps_at = [ii for ii in range(len(instr)) if instr[ii][0] == "jmp"]

print(f"Part 2: ", end="")
for ii in nops_at:
    instr_mod = deepcopy(instr)
    instr_mod[ii][0] = "jmp"
    ret = run(instr_mod)
    if ret[0] == 0:
        print(f"Fixed loop: acc = '{ret[1]}'")
        break

for ii in jmps_at:
    instr_mod = deepcopy(instr)
    instr_mod[ii][0] = "nop"
    ret = run(instr_mod)
    if ret[0] == 0:
        print(f"Fixed loop: acc = '{ret[1]}'")
        break
