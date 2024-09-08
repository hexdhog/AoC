#!/usr/bin/env python3

import sys

# from collections import deque
# from itertools import zip_longest

def parse(a, b): return list(a), tuple(map(int, b.split(",")))
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
  while True:
    out = [range(p, p+n) for p, n in zip(pos, nums)]
    fix = [i for i, c in enumerate(sprs) if c == "#" and all(i not in r for r in out)]
    if len(fix) == 0: break
    pidx = [max(i for i in range(len(out)) if out[i][-1] < f) for f in fix]
    for i, f in zip(pidx[::-1], fix[::-1]): pos[i] = simplefind(sprs, nums[i:i+1], f-nums[i], 0, reverse)[0]
  return pos

def tostr(spr, num, pos):
  tmp = list(spr)
  for i, p in enumerate(pos):
    for j in range(p, p+num[i]):
      if j < len(tmp): tmp[j] = "#"
  return "".join(tmp).replace("?", ".")

for sprs, nums in data:
  # print("".join(sprs), *nums)
  pos = find(sprs, nums)
  s = tostr(sprs, nums, pos)
  check = tuple(len(x) for x in filter(None, s.split("."))) # type: ignore[var-annotated]
  assert check == nums






  # c = tuple(len(x) for x in filter(None, s.split(".")))
  # assert c == nums
  # print(i := i + 1)
  # print()
  # q: deque = deque([find(sprs, nums), []])
  # cnt = 0
  # while len(q) > 0:
  #   x = q.pop()

  #   spr, num = (a[b:] for a, b in zip((sprs, nums), x))
  #   pos = find(spr, num)
  #
  #   print(base, x, spr, num, pos)
  #   print(" " * (len(sprs) - len(spr)) + tostr(spr, num), len(pos) == len(num))
  #
  #   if len(pos) == len(num):
  #     for i, p in enumerate(pos):
  #       tmp = base + pos[:i], (p+1, i)
  #       q.append(tmp)
  #   if (cnt := cnt + 1) > 20: break
  #   #   for i, p in enumerate(pos):
  #   #     if (x := (p+1, i)) not in hist:
  #   #       hist.add(x)
  #   #       q.append(x)
  # break
  # print()
