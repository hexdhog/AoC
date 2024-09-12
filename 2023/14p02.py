#!/usr/bin/env python3

import sys

grid = [l.strip() for l in sys.stdin]

print("\n".join("".join(x) for x in grid), end="\n\n")

grid = list(map("".join, zip(*grid)))

grid = ["#".join("O" * (c := a.count("O")) + "." * (len(a) - c) for a in r.split("#")) for r in grid]

s = sum(sum(len(grid)-i for i, v in enumerate(r) if v == "O") for r in grid)

grid = list(map("".join, zip(*grid)))
print("\n".join("".join(x) for x in grid), end="\n\n")

print(s)

#  y  x
# -1  0
#  0 -1
#  1  0
#  0  1
