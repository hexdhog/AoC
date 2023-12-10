#!/usr/bin/env python3

import sys

seeds = list(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
tables = [[tuple(map(int, y.split())) for y in list(filter(None, x.split("\n")))[1:]] for x in sys.stdin.read().split("\n\n")]
ranges = set(zip(seeds[::2], seeds[1::2]))

for table in tables:
  new = set()
  for rs, rsz in ranges:
    tmp = set()
    for dst, src, tsz in table:
      s, e = max(rs, src), min(rs+rsz-1, src+tsz-1)
      if e > 0 and e-s > 0: tmp.add((s+dst-src, e-s))
    if len(tmp) == 0: tmp.add((rs, rsz))
    for x in tmp: new.add(x)
  ranges = new

print(min(x[0] for x in ranges))
