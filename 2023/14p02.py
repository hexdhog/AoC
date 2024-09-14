#!/usr/bin/env python3

import sys

grid = tuple(l.strip() for l in sys.stdin)

def load(grid): return sum((len(grid) - i) * r.count("O") for i, r in enumerate(grid))
def cycle(grid):
  for _ in range(4):
    grid = tuple("".join(reversed(x)) for x in zip(*grid))
    grid = tuple("#".join("." * ((len(a)) - (c := a.count("O"))) + "O" * c for a in r.split("#")) for r in grid)
  return grid

N = 1000000000
seen = [grid]
for _ in range(N):
  if (grid := cycle(grid)) in seen: break
  seen.append(grid)

cnt, off = len(seen), seen.index(grid)
itr_left, rep_cnt = N - off, cnt - off
r = itr_left % rep_cnt
print(load(seen[off+r]))
