#!/usr/bin/env python3
from __future__ import annotations

import sys

left, right = list(zip(*((int(a) for a in l.strip().split()) for l in sys.stdin)))
s, cnt = 0, {}
for x in left:
  if x not in cnt: cnt[x] = right.count(x)
  s += x*cnt[x]
print(s)
