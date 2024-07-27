#!/usr/bin/env python3

import sys

MOVS = {
  "|": { (1, 0): ((0, 1), (0, -1)), (-1, 0): ((0, 1), (0, -1)) },
  "-": { (0, 1): ((1, 0), (-1, 0)), (0, -1): ((1, 0), (-1, 0)) },
  "/": { (1, 0): ((0, -1),), (-1, 0): ((0, 1),), (0, 1): ((-1, 0),), (0, -1): ((1, 0),) },
  "\\": { (1, 0): ((0, 1),), (-1, 0): ((0, -1),), (0, 1): ((1, 0),), (0, -1): ((-1, 0),) }
}

grid = [list(x.strip()) for x in sys.stdin.readlines()]
gvis = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))] # type: ignore[var-annotated]

def bounds(x: int, y: int) -> bool: return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

beams = [(0, 0, 1, 0)]
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

print(sum(int(len(y) > 0) for x in gvis for y in x))
