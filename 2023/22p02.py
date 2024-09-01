#!/usr/bin/env python3

import sys

from queue import Queue

blocks = sorted(([int(x) for x in l.strip().replace("~", ",").split(",")] for l in sys.stdin.readlines()), key=lambda x: x[2])

def intxy(a, b): return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for i, block in enumerate(blocks):
  mz = max((b[5]+1 for b in blocks[:i] if intxy(block, b)), default=1)
  block[5], block[2] = block[5] - block[2] + mz, mz

blocks.sort(key=lambda x: x[2])

N = len(blocks) + 1
g = [[0 for _ in range(N)] for _ in range(N)]
bi = next(i for i, b in enumerate(blocks) if b[2] > 1) # base blocks end index
for i in range(len(blocks[:bi])): g[0][i+1] = 1
for i, block in enumerate(blocks):
  nli = next((j for j in range(i+1, len(blocks)) if blocks[j][2] > block[5] + 1), len(blocks)) # next level end index
  for j in range(i+1, nli):
    if intxy(block, blocks[j]): g[i+1][j+1] = 1

def supported(g, dis, root=0):
  q: Queue = Queue()
  q.put(root)
  vis = [0 for _ in range(len(g))]
  while not q.empty():
    i = q.get()
    if i in dis: continue
    if vis[i] == 0:
      for j, s in enumerate(g[i]):
        if s == 1: q.put(j)
      vis[i] = 1
  return vis

t = 0
for i in range(len(blocks)):
  v = supported(g, {i+1})
  t += len(v) - sum(v) - 1
print(t)
