#!/usr/bin/env python3

import sys

# from collections import deque
# from itertools import zip_longest

def parse(a, b): return list(a), tuple(map(int, b.split(",")))
data = [parse(*l.strip().split()) for l in sys.stdin.readlines()]

def find(sprs, nums, sproff = 0, numoff = 0, reverse=False):
  if reverse: sprs, nums = sprs[::-1], nums[::-1]
  pos, si, ni = [], sproff, numoff
  while si < len(sprs) and ni < len(nums):
    spre, spr = sprs[se] if (se := si + nums[ni]) < len(sprs) else "", sprs[si:se]
    if len(spr) == nums[ni] and "." not in spr and spre != "#":
      pos.append(si)
      si, ni = se, ni + 1
    si += 1
  return pos if not reverse else [len(sprs) - p - nums[i] - 1 for i, p in enumerate(pos)][::-1]

# def inwrdf(x): return (x := x + 1) // 2 * (1 if x % 2 != 0 else -1)
# def inwrd(l): return (inwrdf(x) for x in range(l))
# def _find(sprs, nums):
#   pos = []
#   ss, se, ni = 0, len(sprs) - 1, 0
#   while ss <= se and ni < len(nums):
#     n = inwrdf(ni)
#     s = ss if n >= 0 else se
#   return pos

def tostr(spr, num, pos):
  tmp = list(spr)
  for i, p in enumerate(pos):
    for j in range(p, p+num[i]):
      if j < len(tmp): tmp[j] = "#"
  return "".join(tmp).replace("?", ".")

for sprs, nums in data:
  print("".join(sprs), *nums)
  pos = find(sprs, nums)
  s = tostr(sprs, nums, pos)
  print(s)
  # check = [len(x) for x in filter(None, s.split("."))] # type: ignore[var-annotated]
  # fix = [i - 1 for i, v in enumerate(zip_longest(nums, check)) if v[0] != v[1]]
  # print(check)
  # print(fix)
  # print(pos)







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
