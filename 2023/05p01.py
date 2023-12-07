#!/usr/bin/env python3

from __future__ import annotations

import sys

class Map:
  def __init__(self, table: list[tuple], child: Map | None = None): self.table, self.child = table, child
  def resolve(self, value: int) -> int:
    for dst, src, length in self.table:
      if src <= value <= src + length:
        value = value + dst - src
        break
    return value if self.child is None else self.child.resolve(value)

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
fmap = None
for table in reversed([[tuple(map(int, y.split())) for y in x[1:]] for x in split([x.strip() for x in sys.stdin.readlines()], "")]): fmap = Map(table, fmap)
assert fmap is not None
print(min(map(fmap.resolve, seeds)))
