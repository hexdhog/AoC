#!/usr/bin/env python3

from __future__ import annotations

import sys

from copy import deepcopy
from collections import deque

matrix = [list(x.strip()) for x in sys.stdin.readlines()]
N = len(matrix) * len(matrix[0])
adj = [[0] * N for _ in range(N)]

COORD = (-1, 0), (1, 0), (0, 1), (0, -1)
SRC = ("S", "|", "L", "J"), ("S", "|", "7", "F"), ("S", "-", "L", "F"), ("S", "-", "7", "J")
DST = ("|", "7", "F"), ("|", "L", "J"), ("-", "7", "J"), ("-", "L", "F")
REPLACE = { "|": "┃", "7": "┓", "F": "┏", "L": "┗", "J": "┛", "-": "━" }
ADJ = { 0b1100: "|", 0b0011: "-", 0b0101: "7", 0b1010: "L", 0b0110: "F", 0b1001: "J" }

start = 0
for y in range(len(matrix)):
  for x in range(len(matrix[y])):
    if matrix[y][x] == ".": continue
    if matrix[y][x] == "S": start = y * len(matrix[y]) + x
    for i in range(len(COORD)):
      adjy, adjx = y + COORD[i][0], x + COORD[i][1]
      if not (0 <= adjy < len(matrix) and 0 <= adjx < len(matrix[y])): continue
      if matrix[y][x] in SRC[i] and matrix[adjy][adjx] in DST[i]: adj[y * len(matrix[y]) + x][adjy * len(matrix[y]) + adjx] = 1

def bfs(mat: list, root: int) -> list:
  length, queue = [0] * len(mat), deque([root])
  while queue:
    node = queue.popleft()
    for i in range(len(mat[node])):
      if mat[node][i] == 1 and length[i] == 0:
        length[i] = length[node] + 1
        queue.append(i)
  return length

# create image matrix for visualization
image = deepcopy(matrix)
for y in range(len(image)):
  for x in range(len(image[y])):
    if any(v == 1 for v in adj[y * len(image[y]) + x]) and image[y][x] in REPLACE: image[y][x] = REPLACE[image[y][x]]
    elif image[y][x] != "S": image[y][x] = "."

loop = bfs(adj, start)

# remove non main loop pipes
for i in range(len(loop)):
  if loop[i] == 0 and i != start:
    y, x = divmod(i, len(image[0]))
    image[y][x], matrix[y][x] = ".", "."

# replace S with appropiate pipe
starty, startx = divmod(start, len(matrix[0]))
start_key = 0
for i in range(len(COORD)):
  adjy, adjx = starty + COORD[i][0], startx + COORD[i][1]
  start_key |= int(0 <= adjy < len(matrix) and 0 <= adjx < len(matrix[starty]) and matrix[adjy][adjx] in DST[i]) << i
matrix[starty][startx] = ADJ[start_key]
image[starty][startx] = REPLACE[ADJ[start_key]]

# ray casting to detect count points inside main loop
cnt = 0
for i in range(len(loop)):
  if loop[i] == 0 and i != start:
    y, x = divmod(i, len(image[0]))
    if len("".join(matrix[y][:x]).replace("-", "").replace(".", "").replace("FJ", "|").replace("L7", "|")) % 2 == 1:
      image[y][x] = "I"
      cnt += 1

print("\n".join("".join(map(str, x)) for x in image), end="\n\n")
print(cnt)
