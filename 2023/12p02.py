#!/usr/bin/env python3

import sys

from collections import deque

def parse(a, b): return list("?".join(a for _ in range(5))), tuple(map(int, b.split(","))) * 5
data = [parse(*l.strip().split()) for l in sys.stdin.readlines()]

def simplefind(sprs, nums, sproff = 0, numoff = 0, reverse=False):
  if reverse: sprs, nums = sprs[::-1], nums[::-1]
  pos, si, ni = [], sproff, numoff
  while si < len(sprs) and ni < len(nums):
    ss, se = si - 1, si + nums[ni]
    sprb, spr, spre = sprs[ss] if ss >= 0 else "", sprs[si:se], sprs[se] if se < len(sprs) else ""
    if len(spr) == nums[ni] and "." not in spr and "#" not in (sprb, spre):
      pos.append(si)
      si, ni = se, ni + 1
    si += 1
  return pos if not reverse else [len(sprs) - p - nums[i] - 1 for i, p in enumerate(pos)][::-1]

def find(sprs, nums, sproff = 0, numoff = 0, reverse=False):
  pos = simplefind(sprs, nums, sproff, numoff, reverse)
  # print(pos, nums[numoff:])
  if len(pos) == len(nums[numoff:]):
    while True:
      out = [range(p, p+n) for p, n in zip(pos, nums[numoff:])]
      fix = [i for i, c in enumerate(sprs) if i >= sproff and c == "#" and all(i not in r for r in out)]
      pidx = [m for f in fix if (m := max((numoff + i for i in range(len(out)) if out[i][-1] < f), default=-1)) >= 0]
      if len(pidx) == 0: break
      for i, f in zip(pidx[::-1], fix[::-1]):
        tmp = simplefind(sprs, nums[i:i+1], f-nums[i], 0, reverse)
        if len(tmp) == 0: return pos[:i-numoff]
        pos[i-numoff] = tmp[0]
  return pos

def tostr(sprs, nums, pos):
  tmp = list(sprs)
  for n, p in zip(nums, pos):
    for i in range(p, p+n):
      if i < len(tmp): tmp[i] = "#"
  return "".join(tmp).replace("?", ".")

res = 0
for sprs, nums in data:
  q: deque = deque([([], 0)])
  cnt = 0
  while len(q) > 0:
    base, sproff = q.pop()
    numoff = len(base)
    pos = find(sprs, nums, sproff, numoff)
    tmp = base + pos
    s = tostr(sprs, nums, tmp)
    check = len(tmp) == len(nums) and nums == tuple(len(x) for x in filter(None, s.split("."))) # type: ignore[var-annotated]
    if check:
      cnt += 1
      for i, p in enumerate(pos): q.append((base + pos[:i], p + 1))
  res += cnt

print(res)
