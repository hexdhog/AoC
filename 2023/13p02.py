#!/usr/bin/env python3

import sys

grid = [list(filter(None, x.split("\n"))) for x in sys.stdin.read().split("\n\n")]

def findv(m: list) -> int:
  for i in range(1, len(m)):
    top, btm = m[:i][::-1], m[i:]
    if sum(int(a != b) for x, y in zip(top[:len(btm)], btm[:len(top)]) for a, b in zip(x, y)) == 1: return i
  return 0

print(sum(findv(["".join(x) for x in zip(*m)]) + 100*findv(m) for m in grid))
