#!/usr/bin/env python3

from __future__ import annotations

import sys

from itertools import pairwise

hist = filter(None, (list(map(int, x.strip().split(" "))) for x in sys.stdin.readlines()))

def diff(l: list) -> list: return [b - a for a, b in pairwise(l)]
def predict(l: list) -> int:
  r = 0
  while any(x != 0 for x in l):
    r += l[-1]
    l = diff(l)
  return r

print(sum(predict(h) for h in hist))
