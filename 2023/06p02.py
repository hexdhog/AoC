#!/usr/bin/env python3

import sys

t = int("".join(sys.stdin.readline().strip().split(":")[-1].split()))
d = int("".join(sys.stdin.readline().strip().split(":")[-1].split()))
print(len([x for x in range(1, t) if (t-x) * x > d]))
