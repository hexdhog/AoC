#!/usr/bin/env python3

import sys

BOUNDS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,+1),(1,-1),(1,0),(1,1)]
def issymbol(mat: list, i: int, j: int) -> bool: return mat[i][j] != "." and not str.isdigit(mat[i][j])

mat = [list(l.strip()) for l in sys.stdin.readlines()]
sel = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
for i in range(len(mat)):
  for j in range(len(mat[i])):
    if not str.isdigit(mat[i][j]): continue
    for b in BOUNDS:
      if issymbol(mat, max(min(i+b[0], len(mat[i])-1), 0), max(min(j+b[1], len(mat[i])-1), 0)):
        sel[i][j] = 1
        break

s = 0
for i in range(len(mat)):
  for j in range(len(mat[i])):
    if not sel[i][j]: continue
    n = mat[i][j]
    for _j in range(j+1, len(mat)):
      if not str.isdigit(mat[i][_j]): break
      n += mat[i][_j]
      sel[i][_j] = 0
    for _j in range(j-1, -1, -1):
      if not str.isdigit(mat[i][_j]): break
      n = mat[i][_j] + n
      sel[i][_j] = 0
    s += int(n)

print(s)
