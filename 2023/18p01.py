#!/usr/bin/env python3

from __future__ import annotations

import sys

DIR = { "L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }

def mov(p: tuple, dp: tuple) -> tuple: return tuple(a+b for a, b in zip(p, dp))
def mul(p: tuple, m: int) -> tuple: return tuple(m*x for x in p)

steps = [mul(DIR[a], int(b)) for a, b, *_ in (x.strip().split() for x in sys.stdin.readlines())]
# print(steps)

pos = (0, 0)
path = [pos] + [pos := mov(pos, s) for s in steps]

xmin, xmax = min(path, key=lambda a: a[0])[0], max(path, key=lambda a: a[0])[0]
ymin, ymax = min(path, key=lambda a: a[1])[1], max(path, key=lambda a: a[1])[1]

view = [[0 for _ in range(xmax-xmin+1)] for _ in range(ymax-ymin+1)]
vert = [[0 for _ in range(xmax-xmin+1)] for _ in range(ymax-ymin+1)]
x, y = abs(xmin), abs(ymin)
for sx, sy in steps:
  tx, ty = mov((x, y), (sx, sy))
  dx, dy = tx - x, ty - y
  if dx != 0:
    for i in range(x, x+dx, int(dx/abs(dx))): view[y][i] = 1
  if dy != 0:
    d = int(dy/abs(dy))
    for i in range(y, y+dy, d): view[i][x], vert[i][x] = 1, d
    vert[ty][tx] = d
  x, y = tx, ty

print("\n".join("".join("#" if y else " " for y in x) for x in view), end="\n\n")
# print("\n".join("".join(" " if y == 0 else ("v" if y > 0 else "^") for y in x) for x in vert), end="\n\n")

def group(l) -> list:
  t: list = []
  for v in iter(l):
    if len(t) != 0 and t[-1] != v: yield t; t = []
    t.append(v)
  if len(t) > 0: yield t

# ray tracing algorithm to determine which blocks are inside the lagoon
for i in range(len(view)):
  for j in range(len(view[i])):
    # abusing the fact that, in this problem, every vertical line must have another one in opposing direction
    # so, if there are x lines in the top-bottom direction, there must be x lines in the bottom-up direction
    if sum(y[0] for y in group(x for x in vert[i][j:] if x != 0)) != 0: view[i][j] = 1

print("\n".join("".join("#" if y else " " for y in x) for x in view), end="\n\n")
print(sum(x for y in view for x in y))
