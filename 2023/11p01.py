#!/usr/bin/env python3

from __future__ import annotations

import sys

from itertools import chain

def chke(m: list) -> bool: return all(x == "." for x in m) # check if row should be expanded
def exph(m: list) -> list: return list(chain(*([x] * (2 if chke(x) else 1) for x in m))) # expand rows
img = [list(x.strip()) for x in sys.stdin.readlines()]
exp = list(zip(*exph(list(zip(*exph(img)))))) # run exph, transpose, run exph and transpose
crd = [(x, y) for y in range(len(exp)) for x in range(len(exp[y])) if exp[y][x] == "#"] # galaxy coordinates
print(sum(sum(abs(crd[i][k] - crd[j][k]) for k in range(2)) for i in range(len(crd)) for j in range(i+1, len(crd))))
