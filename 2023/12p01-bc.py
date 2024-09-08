#!/usr/bin/env python3

import sys

from math import factorial

def parse(a, b): return list(filter(None, a.split("."))), tuple(map(int, b.split(",")))
data = [parse(*l.strip().split()) for l in sys.stdin.readlines()]

def find(sprs, nums):
  si, ni = 0, 0
  pos = []
  while si < len(sprs) and ni < len(nums):
    se = si + nums[ni]
    sprb, spr, spre = sprs[si-1] if si-1 >= 0 else "", sprs[si:se], sprs[se] if se < len(sprs) else ""
    if len(spr) == nums[ni] and "." not in spr and "#" not in (sprb, spre):
      pos.append(si)
      si, ni = se, ni + 1
    si += 1
  return pos

def bc(n, k): return factorial(n) / (factorial(k) * factorial(n - k))

def match(sprg, nums, reverse=False):
  if reverse: sprg, nums = sprg[::-1], nums[::-1]
  npos, off = [], 0
  for spr in sprg:
    e = max((i for i, c in enumerate(spr) if c == "#"), default=len(spr))
    f = find(spr, nums[off:])
    npos.append(set(range(off, off+len(f))))
    f = [x for x in f if x <= e]
    if e != len(spr): off += len(f)
  return npos if not reverse else [{len(nums) - y - 1 for y in x} for x in npos[::-1]]

for sprg, nums in data:
  print(sprg, nums)
  fwd, bak = match(sprg, nums), match(sprg, nums, reverse=True)
  m = [a | b for a, b in zip(fwd, bak)]
  # print(fwd)
  # print(bak)
  print(m)
  # break
