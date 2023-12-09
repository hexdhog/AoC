#!/usr/bin/env python3

from __future__ import annotations

import sys

# def union(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
#   s, e = min(a[0], b[0]), max(a[1], b[1])
#   return (s, e) if s < e else (0, 0)

def inter(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
  s, e = max(a[0], b[0]), min(a[1], b[1])
  return (s, e) if s < e else (0, 0)

# all of the elements of b which are not in a
def compl(a: tuple[int, int], b: tuple[int, int]) -> tuple[tuple[int, int], ...]:
  i = inter(a, b)
  if i == (0, 0): return ((0, 0), b)
  if i == a: return ((b[0], a[0]-1), (a[1]+1, b[1]))
  if i == b: return ((0, 0), (0, 0))
  if a[0] < b[0]: return ((0, 0), (a[1]+1, b[1]))
  return ((0, 0), (b[0], a[0]-1))

seeds = list(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
tables = [[tuple(map(int, y.split())) for y in list(filter(None, x.split("\n")))[1:]] for x in sys.stdin.read().split("\n\n")]

ranges = set(zip(seeds[::2], seeds[1::2]))

for table in tables:
  print(ranges)
  new = set()
  for rs, rsz in ranges:
    tmp = set()
    for dst, src, tsz in table:
      re, os, oe = rs+rsz, max(rs, src), min(rs+rsz, src+tsz)
      if os >= oe: continue
      elif rs >= os and re <= oe:
        tmp.add((rs+dst-src, rsz))
      elif rs <= os and oe <= re:
        tmp.add((rs, os-rs))
        tmp.add((dst, oe-os))
        tmp.add((oe, rs+rsz-oe))
      elif rs <= os and re <= oe:
        tmp.add((rs, re-os))
        tmp.add((dst, oe-os))
      elif rs >= os and re >= oe:
        tmp.add((dst+rs-src, oe-os))
        tmp.add((oe, re-oe))
    if len(tmp) == 0: tmp.add((rs, rsz))
    for x in tmp: new.add(x)
  ranges = set(filter(lambda x: x[1] != 0, new))

print()
print(ranges)
# print(min(ranges, key=lambda x: x[0]))
