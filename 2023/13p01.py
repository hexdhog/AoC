#!/usr/bin/env python3

import sys

grid = [list(filter(None, x.split("\n"))) for x in sys.stdin.read().split("\n\n")]

def findv(m: list) -> int:
  for i in range(1, len(m)):
    t, b = m[:i][::-1], m[i:]
    if t[:len(b)] == b[:len(t)]: return i
  return 0

print(sum(findv(["".join(x) for x in zip(*m)]) + 100*findv(m) for m in grid))
