#!/usr/bin/env python3

import sys

# based off of the brilliant solution: https://github.com/maksverver/AdventOfCode/blob/master/2023/day12/solve-dp.py

M = 5
def parse(l):
  a, b = l.strip().split()
  return "?".join([a] * M) + ".", tuple(map(int, b.split(","))) * M
data = list(map(parse, sys.stdin))

def comb(sprs, nums):
  mhash = [0] * (len(sprs)+1)
  for i, c in enumerate(sprs):
    if c != ".": mhash[i+1] = mhash[i] + 1

  cnt = [[1] * ((l := len(sprs.split("#")[0])) + 1) + [0] * (len(sprs) - l)]
  cnt += [[0] * (len(sprs)+1) for _ in range(len(nums))]

  for i, n in enumerate(nums):
    for j, c in enumerate(sprs):
      if c != "#":
        cnt[i+1][j+1] = cnt[i+1][j] + (n <= mhash[j] and cnt[i][max(j-n, 0)])
  return cnt[len(nums)][len(sprs)]

print(sum(comb(sprs, nums) for sprs, nums in data))
