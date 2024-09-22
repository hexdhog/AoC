#!/usr/bin/env python3

from __future__ import annotations

import sys

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def scale(p: tuple, m: int) -> tuple: return tuple(m*x for x in p)
def mul(a: tuple, b: tuple) -> tuple: return tuple(x*y for x, y in zip(a, b))
def add(s: tuple, e: tuple) -> tuple: return tuple(a+b for a, b in zip(s, e))
def diff(s: tuple, e: tuple) -> tuple: return add(e, scale(s, -1))
def pdir(s: tuple, e: tuple) -> tuple: return tuple(x // abs(x) if x != 0 else 0 for x in diff(s, e))
def polyarea(v: list) -> float: return sum((v[i][1]+v[i+1][1])*(v[i][0]-v[i+1][0]) for i in range(len(v)-1)) / 2.0

def parse(s: str) -> tuple:
  s = s.strip("(#)")
  return DIR[int(s[5])], int(s[:5], 16)

steps = [parse(x.strip().split()[2]) for x in sys.stdin.readlines()]
path = [pos := (0, 0)] + [pos := add(pos, mul(d, (s, s))) for d, s in steps]

vert, voff = [path[0]], path[0]
for i in range(len(vert), len(path)-1):
  src, dst = pdir(path[i-1], path[i]), pdir(path[i], path[i+1])
  case, mask = abs(sum(src) + sum(dst)) // 2, tuple(abs(a) for a in src)
  base = mul(voff, mask[::-1])
  voff = (sum(base),) * 2
  if case == 1: voff = add(base, mul(mask, tuple(int(not a) for a in voff)))
  vert.append(add(path[i], voff))
vert.append(vert[0])
print(int(polyarea(vert)))
