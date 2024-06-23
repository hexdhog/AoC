#!/usr/bin/env python3

from __future__ import annotations

import sys

lines = filter(None, (x.strip() for x in sys.stdin.readlines()))
order = next(lines)
table = { y: dict(zip(("L", "R"), z.strip("()").split(", "))) for y, z in (x.split(" = ") for x in lines)}
curr, target, i = "AAA", "ZZZ", 0
while curr != target: curr, i = table[curr][order[i % len(order)]], i + 1
print(i)
