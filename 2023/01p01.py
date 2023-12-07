#!/usr/bin/env python3

import sys

print(sum(x[0] * 10 + x[-1] for x in (tuple(map(int, filter(str.isdigit, x))) for x in sys.stdin.readlines())))
