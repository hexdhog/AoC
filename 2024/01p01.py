#!/usr/bin/env python3

import sys

left, right = [sorted(x) for x in zip(*((int(a) for a in l.strip().split()) for l in sys.stdin))]
print(sum(abs(a-b) for a, b in zip(left, right)))
