#!/usr/bin/env python3

import sys

DEBUG = False
MOVS = {(1, 0), (-1, 0), (0, 1), (0, -1)}

grid = [list(l.strip()) for l in sys.stdin.readlines()]
sx, sy = next((r.index("S"), y) for y, r in enumerate(grid) if "S" in r)

if DEBUG:
  print("\n".join("".join(x) for x in grid), end="\n\n")
  print(f"S -> x: {sx}; y: {sy}")

def gstep(c, cmin, cmax): return c if c == 0 else c // abs(c) * int(not cmin <= c < cmax)
def neigbours(gx, gy, px, py):
  for nx, ny in ((px + dx, py + dy) for dx, dy in MOVS):
    if grid[y := ny % len(grid)][x := nx % len(grid[py])] != "#": yield (gx + gstep(nx, 0, len(grid[y])), gy + gstep(ny, 0, len(grid))), (x, y)

def step(gmap):
  tmp: dict = {}
  for gpos, pos in gmap.items():
    for p in pos:
      for gp, pp in neigbours(*(gpos+p)):
        if gp not in tmp: tmp[gp] = set()
        tmp[gp].add(pp)
  return tmp


gmap = { (0, 0): {(sx, sy)} }
for _ in range(100): gmap = step(gmap)
# for _ in range(26501365): gmap = step(gmap)

if DEBUG:
  for gp, pos in gmap.items():
    g = [l.copy() for l in grid]
    for x, y in pos: g[y][x] = "O"
    print(gp)
    print("\n".join("".join(x) for x in g), end="\n\n")

print(sum(len(pos) for pos in gmap.values()))
