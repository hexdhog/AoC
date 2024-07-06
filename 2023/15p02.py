#!/usr/bin/env python3

import sys

from functools import reduce

def ahash(s: str) -> int: return reduce(lambda x, c: ((x + ord(c)) * 17) % 256, (0, *s))

boxes = [{} for _ in range(256)] # type: ignore[var-annotated]
for step in sys.stdin.readline().strip().split(","):
  n = ahash(l := "".join(filter(str.isalpha, step)))
  op = "".join(filter(lambda x: not str.isalpha(x), step))
  if op == "-" and l in boxes[n]: del boxes[n][l]
  elif "=" in op: boxes[n][l] = int(op[1:])

print(sum((i+1)*(j+1)*v for i, box in enumerate(boxes) for j, v in enumerate(box.values())))
