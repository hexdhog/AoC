#!/usr/bin/env python3

from __future__ import annotations

import sys

from functools import reduce
from itertools import pairwise

hist = filter(None, (list(map(int, x.strip().split(" "))) for x in sys.stdin.readlines()))

def diff(l: list) -> list: return [b - a for a, b in pairwise(l)]
def predict(l: list) -> int:
  r = []
  while any(x != 0 for x in l):
    r.append(l[0])
    l = diff(l)
  return reduce(lambda a, b: b - a, [0, *r[::-1]])

print(sum(predict(h) for h in hist))
