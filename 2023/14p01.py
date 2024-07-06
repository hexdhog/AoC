#!/usr/bin/env python3

import sys

grid = [list(x.strip()) for x in sys.stdin.readlines()]
grid = list(map(list, zip(*grid)))

s = 0
for c in grid:
  for i in range((len(c)-1) * (len(c)-1)):
    i %= len(c)-1
    if c[i] == "." and c[i+1] == "O": c[i], c[i+1] = c[i+1], c[i]
  s += sum(len(grid)-i for i, v in enumerate(c) if v == "O")

print(s)
