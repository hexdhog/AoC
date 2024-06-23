#!/usr/bin/env python3

from __future__ import annotations

import sys

from math import gcd
from functools import reduce

lines = filter(None, (x.strip() for x in sys.stdin.readlines()))
order = next(lines)
table = { y: dict(zip(("L", "R"), z.strip("()").split(", "))) for y, z in (x.split(" = ") for x in lines)}
nodes = list(table.keys())
start = filter(lambda x: x[-1] == "A", nodes)

def pcnt(node: str) -> int:
  i = 0
  while node[-1] != "Z": node, i = table[node][order[i % len(order)]], i + 1
  return i

print(reduce(lambda a, b: int(a * b / gcd(a, b)), (pcnt(x) for x in start))) # least common multiple of all paths
