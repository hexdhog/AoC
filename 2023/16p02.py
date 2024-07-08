#!/usr/bin/env python3

import sys

from itertools import product

MOVS = {
  "|": { (1, 0): ((0, 1), (0, -1)), (-1, 0): ((0, 1), (0, -1)) },
  "-": { (0, 1): ((1, 0), (-1, 0)), (0, -1): ((1, 0), (-1, 0)) },
  "/": { (1, 0): ((0, -1),), (-1, 0): ((0, 1),), (0, 1): ((-1, 0),), (0, -1): ((1, 0),) },
  "\\": { (1, 0): ((0, 1),), (-1, 0): ((0, -1),), (0, 1): ((1, 0),), (0, -1): ((-1, 0),) }
}

grid = [list(x.strip()) for x in sys.stdin.readlines()]
def bounds(x: int, y: int) -> bool: return all(0 <= a < b for a, b in ((x, len(grid[0])), (y, len(grid))))

START = [[product((0,), range(len(grid[0]))), (1, 0)],
         [product((len(grid)-1,), range(len(grid[0]))), (-1, 0)],
         [product(range(len(grid[0])), (0,)), (0, 1)],
         [product(range(len(grid[0])), (len(grid)-1,)), (0, -1)]]

m = 0
for spos, sdir in START:
  for pos in spos:
    gvis = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))] # type: ignore[var-annotated]
    beams = [(pos[0], pos[1], sdir[0], sdir[1])]
    gvis[beams[0][1]][beams[0][0]].add(tuple(beams[0][2:]))
    while len(beams) > 0:
      tmp = [] # type: ignore[var-annotated]
      for beam in beams:
        x, y, dx, dy = beam
        if dirs := MOVS.get(grid[y][x], {}).get((dx, dy), None): tmp += [(x+d[0], y+d[1], *d) for d in dirs] # type: ignore[attr-defined]
        else: tmp.append((x+dx, y+dy, dx, dy))
      beams.clear()
      for x, y, dx, dy in tmp:
        if not bounds(x, y) or (dx, dy) in gvis[y][x]: continue
        gvis[y][x].add((dx, dy))
        beams.append((x, y, dx, dy))
    m = max(m, sum(int(len(y) > 0) for x in gvis for y in x))

print(m)
