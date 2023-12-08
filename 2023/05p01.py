#!/usr/bin/env python3

from __future__ import annotations

import sys
from functools import reduce

def resolve(table: list, value: int) -> int:
  for dst, src, length in table:
    if src <= value <= src + length: return value + dst - src
  return value

def split(l: list, check: object) -> list:
  ret, tmp = [], [] # type: ignore[var-annotated]
  for e in l:
    if e == check:
      if len(tmp) > 0: ret.append(tmp)
      tmp = []
    else:
      tmp.append(e)
  ret.append(tmp)
  return ret

seeds = tuple(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
tables = [[tuple(map(int, y.split())) for y in x[1:]] for x in split([x.strip() for x in sys.stdin.readlines()], "")]
print(min(reduce(lambda v, t: resolve(t, v), [seed, *tables]) for seed in seeds)) # type: ignore[arg-type,type-var]
