#!/usr/bin/env python3

from __future__ import annotations

import sys

from collections import deque

matrix = [list(x.strip()) for x in sys.stdin.readlines()]
N = len(matrix) * len(matrix[0])
adj = [[0] * N for _ in range(N)]

COORD = (-1, 0), (1, 0), (0, 1), (0, -1)
SRC = ("S", "|", "L", "J"), ("S", "|", "7", "F"), ("S", "-", "L", "F"), ("S", "-", "7", "J")
DST = ("|", "7", "F"), ("|", "L", "J"), ("-", "7", "J"), ("-", "L", "F")

start = 0
for y in range(len(matrix)):
  for x in range(len(matrix[y])):
    if matrix[y][x] == ".": continue
    if matrix[y][x] == "S": start = y * len(matrix[0]) + x
    for i in range(len(COORD)):
      adjy, adjx = y + COORD[i][0], x + COORD[i][1]
      if not (0 <= adjy < len(matrix) and 0 <= adjx < len(matrix[y])): continue
      if matrix[y][x] in SRC[i] and matrix[adjy][adjx] in DST[i]: adj[y * len(matrix[0]) + x][adjy * len(matrix[y]) + adjx] = 1

def bfs(mat: list, root: int) -> list:
  length, queue = [0] * len(mat), deque([root])
  while queue:
    node = queue.popleft()
    for i in range(len(mat[node])):
      if mat[node][i] == 1 and length[i] == 0:
        length[i] = length[node] + 1
        queue.append(i)
  return length

print(max(bfs(adj, start)))
