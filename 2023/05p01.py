#!/usr/bin/env python3

from __future__ import annotations

import sys

class Map:
  def __init__(self, table: list[tuple[int, int, int]], child: Map | None = None): self.table, self.child = table, child
  def resolve(self, value: int) -> int: return value

seeds = tuple(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
for l in [x.strip() for x in sys.stdin.readlines()]:
  print(l)
