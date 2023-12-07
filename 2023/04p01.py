#!/usr/bin/env python3

import sys

data = [l.strip() for l in sys.stdin.readlines()]
s = 0
for card in data:
  c, n = card.split(":")
  cn = int(c.split()[-1])
  w, h = (list(map(int, x.split())) for x in n.split("|"))
  s += int(2**(len([x for x in w if x in h])-1))
print(s)
