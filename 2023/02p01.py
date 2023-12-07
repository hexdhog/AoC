#!/usr/bin/env python3

from __future__ import annotations

import sys

CUBES = { "red": 12, "green": 13, "blue": 14 }
def chkgame(g: str) -> tuple:
  gid, s = g.split(":")
  return int(gid.split()[-1]), all(all(CUBES[z[1]] >= int(z[0]) for z in (y[1:].split() for y in x.split(","))) for x in s.split(";"))
print(sum(x[0] for x in filter(lambda x: x[1], (chkgame(l.strip()) for l in sys.stdin.readlines()))))
