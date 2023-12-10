#!/usr/bin/env python3

import sys
from operator import mul
from functools import reduce

times = list(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
distances = list(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
print(reduce(mul, [len([x for x in range(1, times[i]) if (times[i]-x) * x > distances[i]]) for i in range(len(times))]))
