#!/usr/bin/env python3

import sys

from functools import reduce

def ahash(s: str) -> int: return reduce(lambda x, c: ((x + ord(c)) * 17) % 256, (0, *s))
print(sum(ahash(x) for x in sys.stdin.readline().strip().split(",")))
