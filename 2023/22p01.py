#!/usr/bin/env python3

import sys

blocks = sorted(([int(x) for x in l.strip().replace("~", ",").split(",")] for l in sys.stdin.readlines()), key=lambda x: x[2])

def intxy(a, b): return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])

for i, block in enumerate(blocks):
  mz = max((b[5]+1 for b in blocks[:i] if intxy(block, b)), default=1)
  block[5], block[2] = block[5] - block[2] + mz, mz

blocks.sort(key=lambda x: x[2])

s = set()
for i, block in enumerate(blocks):
  sb = [b for j, b in enumerate(blocks) if i != j and b[5] == block[5]]
  tb = (b for b in blocks[i+1:] if b[2] - 1 == block[5])
  fall = [all(not intxy(a, b) for b in sb) for a in tb]
  if len(fall) == 0 or not any(fall): s.add(i)
print(len(s))
