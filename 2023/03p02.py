#!/usr/bin/env python3

from __future__ import annotations

import sys
from operator import mul
from functools import reduce
from typing import Callable

BOUNDS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def clip(val: int, _min: int, _max: int) -> int: return max(min(val, _max), _min)
def bounds(mat: list, i: int, j: int) -> list: return list(dict.fromkeys([(clip(i+_i, 0, len(mat)-1), clip(j+_j, 0, len(mat)-1)) for _i, _j in BOUNDS]))
def cuntil(l: list, off: int, stop: Callable, step: int = 1) -> int:
  ret = off
  for i in range(off, len(l) if step > 0 else -1, step):
    if stop(l[i]): break
    ret = i
  return ret

def until(l: list, off: int, stop: Callable, step: int = 1) -> list:
  ret = []
  for i in range(off, len(l) if step > 0 else -1, step):
    if stop(l[i]): break
    ret.append(l[i])
  return ret

mat = [list(l.strip()) for l in sys.stdin.readlines()]
total = 0
for i in range(len(mat)):
  for j in range(len(mat[i])):
    if mat[i][j] != "*": continue
    c = []
    for x in bounds(mat, i, j):
      if str.isdigit(mat[x[0]][x[1]]):
        s, e = cuntil(mat[x[0]], x[1], lambda y: not str.isdigit(y), -1), cuntil(mat[x[0]], x[1], lambda y: not str.isdigit(y))
        if not any(y in c for y in [(x[0], k) for k in range(s, e+1)]): c.append(x)
    if len(c) < 2: continue
    # print([int("".join(list(reversed(until(mat[_i], _j-1, lambda x: not str.isdigit(x), -1))) + until(mat[_i], _j, lambda x: not str.isdigit(x)))) for _i, _j in c])
    total += reduce(mul, [int("".join(list(reversed(until(mat[_i], _j-1, lambda x: not str.isdigit(x), -1))) + until(mat[_i], _j, lambda x: not str.isdigit(x)))) for _i, _j in c])

print(total)
