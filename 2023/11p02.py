#!/usr/bin/env python3

from __future__ import annotations

import sys

def chke(m: list) -> bool: return all(x == "." for x in m) # check if row should be expanded
def exph(m: list) -> list: return [i for i in range(len(m)) if chke(m[i])] # get indeces of rows to expand

img = [list(x.strip()) for x in sys.stdin.readlines()]
exp = exph(list(zip(*img))), exph(img) # tuple with x, y indeces of rows to expand
crd = [(x, y) for y in range(len(img)) for x in range(len(img[y])) if img[y][x] == "#"] # galaxy coordinates

cnt = 0
for i in range(len(crd)):
  for j in range(i+1, len(crd)):
    for k in range(2):
      s, e = min(crd[i][k], crd[j][k]), max(crd[i][k], crd[j][k])
      cnt += e - s + len([x for x in exp[k] if x in range(s, e)]) * (1000000 - 1)
print(cnt)
