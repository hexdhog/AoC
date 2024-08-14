#!/usr/bin/env python3

from __future__ import annotations

import sys

DIR = { "L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }
DC = ["R", "D", "L", "U"]

def mul(p: tuple, m: int) -> tuple: return tuple(m*x for x in p)
def mov(p: tuple, dp: tuple) -> tuple: return tuple(a+b for a, b in zip(p, dp))

# def parse(s: str) -> tuple:
#   s = s.strip("(#)")
#   return DC[int(s[5])], int(s[:5], 16)
#
# steps = [parse(x.strip().split()[2]) for x in sys.stdin.readlines()]
# print(steps)

steps = [mul(DIR[a], int(b)) for a, b, *_ in (x.strip().split() for x in sys.stdin.readlines())]
print(steps)
print()

pos = (0, 0)
path = [pos] + [pos := mov(pos, s) for s in steps]
print(path)
exp_path = [(0, 0), (7, 0), (7, 6), (5, 6), (5, 7), (7, 7), (7, 10), (1, 10), (1, 8), (0, 8), (0, 5), (2, 5), (2, 3), (0, 3), (0, 0)]
print(exp_path)












# def inc(p: tuple, s: tuple) -> tuple: return p[0] + int(s[0] != 0), p[1] + int(s[1] != 0)
# def dec(p: tuple, s: tuple) -> tuple: return p[0] - int(s[0] != 0), p[1] - int(s[1] != 0)
#
# pos = inc(steps[0], steps[0])
# path = [pos]
# edg = (0, 0)
# for i in range(1, len(steps)-1):
#   # print(f"{pos} + {steps[i]} -> ", end="")
#   pos = mov(pos, steps[i])
#   ori = [a*b < 0 for a, b in zip(steps[i-1], steps[i+1])]
#   # print(f"{pos} [{steps[i-1]} {steps[i+1]} : {ori}]")
#   path.append(pos)
#
# # path = [pos] + [pos := mov(pos, s) for s in steps]
# print(len(path), path)
#
# path = [(7, 0), (7, 6), (5, 6), (5, 7), (7, 7), (7, 10), (1, 10), (1, 8), (0, 8), (0, 5), (2, 5), (2, 3), (0, 3)]
# print(len(path), path)
#
# t = 0
# for i in range(len(path)-1):
#   c, n = path[i], path[i+1]
#   t += c[0]*n[1] - n[0]*c[1]
# print(t/2)
