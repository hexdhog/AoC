#!/usr/bin/env python3

from __future__ import annotations

import sys

# from math import factorial

data = [(y[0], list(map(int, y[1].split(",")))) for y in (x.strip().split(" ") for x in sys.stdin.readlines())]
def disp(d: list): print("\n".join(f"{x:25s} {','.join(map(str, y))}" for x, y in d))
disp(data)
print()

for sprs, cnts in data:
  sprm = 0 # spring string max index for the current count
  for i in range(len(cnts)):
    j, k = sprm, i
    spr = sprs
    while j < len(sprs) and k < len(cnts):
      n = cnts[k]
      tmp = sprs[j:j+n].replace("?", "#")
      if tmp == "#" * n and (j+n >= len(sprs) or sprs[j+n] != "#"):
        spr = spr[:j] + tmp + sprs[j+n:]
        if i == k: sprm = j+n+1
        j, k = j+n, k+1
      j += 1
    if k == len(cnts): print(spr, i)

# def bc(n: int, k: int) -> int: return factorial(n) // (factorial(k)*factorial(n-k))
#
# total = 0
# for sprs, cnts in data:
#   spr, cnt = sprs, []
#   i, j = 0, 0
#   while i < len(sprs) and j < len(cnts):
#     n = cnts[j]
#     if sprs[i:i+n].replace("?", "#") == "#" * n and (i+n >= len(sprs) or sprs[i+n] != "#"):
#       cnt.append(sprs[i:i+n].count("?"))
#       spr = spr[:i] + sprs[i:i+n].replace("?", "x") + sprs[i+n:]
#       i, j = i+n, j+1
#     i += 1
#
#   tmp = [x.split("?") for x in filter(None, spr[spr.index("x"):].split("."))]
#   print(sprs, cnts)
#   print(spr)
#   # print(tmp)
#   s = 1
#   for x in tmp:
#     c = len(list(filter(None, x)))
#     s *= bc(len(x), c)
#     # print(x)
#   print(s)
#   # print()
#   total += s
# print(total)
