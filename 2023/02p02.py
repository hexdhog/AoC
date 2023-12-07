#!/usr/bin/env python3

from __future__ import annotations

import sys

from functools import reduce

def parse(g: str) -> tuple:
  gid, s = g.split(":")
  return int(gid.split()[-1]), (((int(z[0]), z[1]) for z in (y[1:].split() for y in x.split(","))) for x in s.split(";"))

total = 0
for g in (l.strip() for l in sys.stdin.readlines()):
  game, d = parse(g)
  m = {"red": 0, "green": 0, "blue": 0}
  for s in d:
    for x in s:
      m[x[1]] = max(m[x[1]], x[0])
  total += reduce(lambda x, y: x*y, m.values())
print(total)
