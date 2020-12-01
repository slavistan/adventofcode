#!/usr/bin/env python3

def choo_choo(nums, total):
    for ii in range(len(nums)):
        for jj in range(len(nums)):
            if nums[ii] + nums[jj] == total:
                    return (ii, jj)


def choo_choo_choo(nums, total):
    for ii in range(len(nums)):
        for jj in range(len(nums)):
            for kk in range(len(nums)):
                if nums[ii] + nums[jj] + nums[kk] == total:
                    return (ii, jj, kk)


nums = [int(line.rstrip('\n')) for line in open("./input")]

n, m = choo_choo(nums, 2020)
print(f"Duplet:\n\t{nums[n]} + {nums[m]} = 2020\n\t{nums[n]} × {nums[m]} = {nums[n] * nums[m]}\n")

n, m, k = choo_choo_choo(nums, 2020)
print(f"Triplet:\n\t{nums[n]} + {nums[m]} + {nums[k]} = 2020\n\t{nums[n]} × {nums[m]} × {nums[k]} = {nums[n] * nums[m] * nums[k]}\n")

print(r"""
 _________________________________
/ When in doubt, use brute force. \
|                                 |
\ -- Ken Thompson                 /
 ---------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
""")
