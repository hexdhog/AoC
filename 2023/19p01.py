#!/usr/bin/env python3

from __future__ import annotations

import sys

rules: dict[str, list] = {}
def tmp(c, v): return lambda x: x < v if c == "<" else x > v
def parse_cnd(cond):
  if ":" not in cond: return cond
  cnd, dst = cond.split(":")
  return [cnd[0], tmp(cnd[1], int(cnd[2:])), dst]
while l := sys.stdin.readline().strip():
  n, conds = l.split("{")
  rules[n] = [parse_cnd(cond) for cond in conds.strip("}").split(",")]

def nv(t): return t[0], int(t[1])
parts = [dict(nv(x.split("=")) for x in l.strip("\n{}").split(",")) for l in sys.stdin.readlines()]

acc = 0
for part in parts:
  r = "in"
  while r not in ("A", "R"):
    for cnd in rules[r]:
      if isinstance(cnd, str): r = cnd; break
      if cnd[1](part[cnd[0]]): r = cnd[2]; break
  if r == "A": acc += sum(part.values())

print(acc)
