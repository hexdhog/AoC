#!/usr/bin/env python3

import sys

from copy import deepcopy
from collections import deque

MOVS = ((0, -1), (1, 0), (0, 1), (-1, 0))

grid = [list(map(int, list(x.strip()))) for x in sys.stdin.readlines()]
print("\n".join("".join(map(str, x)) for x in grid), end="\n\n")

val = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
pre = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

def bounds(x: int, y: int) -> bool: return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
def bpath(pre: list, x: int, y: int, maxlen: int = -1) -> list:
  r = [(x, y)]
  while (x, y) != (0, 0) and (maxlen < 0 or (maxlen := maxlen - 1) >= 0):
    x, y = pre[y][x]
    r.append((x, y))
  return r

nodes: deque = deque(((0, 0),))
while len(nodes) > 0:
  x, y = nodes.popleft()
  if (x, y) == (len(grid[0])-1, len(grid)-1): break
  path = bpath(pre, x, y, 3)
  pdir = [tuple(a - b for a, b in zip(path[i], path[i+1])) for i in range(len(path)-1)]
  for nx, ny, dx, dy in filter(lambda x: bounds(*x[:2]), (tuple(a + b for a, b in zip((x, y), mov)) + mov for mov in MOVS)):
    if pre[y][x] == (nx, ny): continue

    if len(pdir) >= 3 and all((dx, dy) == pd for pd in pdir): continue

    if (v := val[y][x] + grid[ny][nx]) < val[ny][nx] or val[ny][nx] == 0: val[ny][nx], pre[ny][nx] = v, (x, y)
    if not vis[ny][nx] and (nx, ny) not in nodes: nodes.append((nx, ny))
  vis[y][x] = True


print("\n".join("\t".join(map(str, x)) for x in val), end="\n\n")
# print(val[len(grid)-1][len(grid[0])-1])

def draw(x: int, y: int, sym: str) -> list:
  tmp = deepcopy(grid)
  while (x, y) != (0, 0): tmp[y][x], x, y = sym, *pre[y][x] # type: ignore[misc]
  return tmp

# tmp = list(filter(None, [y for x in pre for y in x]))
# pends = [(x, y) for y in range(len(pre)) for x in range(len(pre[0])) if (x, y) not in tmp]
# for x, y in pends: print("\n".join("".join(map(str, x)) for x in draw(x, y, ".")), end="\n\n")

VIS = { (1, 0): ">", (-1, 0): "<", (0, -1): "^", (0, 1): "v" }
tmp = [[VIS[x-p[0], y-p[1]] if (p := pre[y][x]) else "@" for x in range(len(pre[y]))] for y in range(len(pre))]
print("\n".join("".join(map(str, x)) for x in tmp), end="\n\n")

end = draw(len(grid[0]) - 1, len(grid) - 1, ".")
print("\n".join("".join(map(str, x)) for x in end), end="\n\n")
