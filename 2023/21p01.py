#!/usr/bin/env python3

import sys

from operator import or_
from functools import reduce

DEBUG = False
MOVS = {(1, 0), (-1, 0), (0, 1), (0, -1)}

grid = [list(l.strip()) for l in sys.stdin.readlines()]
sx, sy = next((r.index("S"), y) for y, r in enumerate(grid) if "S" in r)
def bounds(x, y): return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

if DEBUG:
  print("\n".join("".join(x) for x in grid), end="\n\n")
  print(f"S -> x: {sx}; y: {sy}")

def neigbours(x, y): return {(nx, ny) for nx, ny in ((x+dx, y+dy) for dx, dy in MOVS) if bounds(nx, ny) and grid[ny][nx] != "#"}
def step(pos): return reduce(or_, (neigbours(px, py) for px, py in pos))

pos = {(sx, sy)}
for _ in range(64): pos = step(pos)
if DEBUG:
  for x, y in pos: grid[y][x] = "O"
  print("\n".join("".join(x) for x in grid), end="\n\n")
print(len(pos))
