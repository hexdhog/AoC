#!/usr/bin/env python3

from __future__ import annotations

import sys

rules: dict[str, list] = {}
def parse_cnd(cond):
  if ":" not in cond: return cond
  cnd, dst = cond.split(":")
  return [cnd[0], cnd[1], int(cnd[2:]), dst]
while l := sys.stdin.readline().strip():
  n, conds = l.split("{")
  rules[n] = [parse_cnd(cond) for cond in conds.strip("}").split(",")]

print(rules)
print()

paths = [("in", { "x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000) })]

while any(n not in ("A", "R") for n, _ in paths):
  tmp = []
  for i in range(len(paths)):
    rname, part = paths[i]
    if rname in ("A", "R"): continue
    for cond in rules[rname]:
      p, t = part.copy(), cond
      if isinstance(cond, list):
        n, c, v, t = cond
        pmin, pmax = p[n]
        nmin, nmax = pmin, pmax
        if c == "<": nmin = (pmax := min(pmax, v-1)) + 1
        elif c == ">": nmax = (pmin := max(pmin, v+1)) - 1
        if pmin > pmax: continue
        part[n], p[n] = (nmin, nmax), (pmin, pmax)
      tmp.append((t, p))
  paths = tmp

# m = { "x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000) }
t = 0
for _, part in (path for path in paths if path[0] == "A"):
  s = 1
  for pmin, pmax in part.values():
    s *= pmax - pmin + 1
  print(part, s)
  t += s

print()
print(t)
