#!/usr/bin/env python3

import sys

grid = list(map("".join, zip(*(l.strip() for l in sys.stdin))))
grid = ["#".join("O" * (c := a.count("O")) + "." * (len(a) - c) for a in r.split("#")) for r in grid]
print(sum(len(grid)-i for r in grid for i, v in enumerate(r) if v == "O"))
