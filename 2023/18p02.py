#!/usr/bin/env python3

from __future__ import annotations

import sys
import math

# import numpy as np
# import matplotlib.pyplot as plt

DIR = { "L": (-1, 0), "R": (1, 0), "D": (0, 1), "U": (0, -1) }
DC = ["R", "D", "L", "U"]

def scale(p: tuple, m: int) -> tuple: return tuple(m*x for x in p)
def mul(a: tuple, b: tuple) -> tuple: return tuple(x*y for x, y in zip(a, b))
def mov(p: tuple, dp: tuple) -> tuple: return tuple(a+b for a, b in zip(p, dp))

# def parse(s: str) -> tuple:
#   s = s.strip("(#)")
#   return DC[int(s[5])], int(s[:5], 16)
#
# steps = [parse(x.strip().split()[2]) for x in sys.stdin.readlines()]
# print(steps)

steps = [scale(DIR[a], int(b)) for a, b, *_ in (x.strip().split() for x in sys.stdin.readlines())]
print(steps)
path = [pos := (0, 0)] + [pos := mov(pos, s) for s in steps]
print(path)
# exp_path = [(0, 0), (7, 0), (7, 6), (5, 6), (5, 7), (7, 7), (7, 10), (1, 10), (1, 8), (0, 8), (0, 5), (2, 5), (2, 3), (0, 3), (0, 0)]
# print(exp_path)

def ldir(s, e): return mov(e, scale(s, -1))
def mag(a): return math.sqrt(sum(b**2 for b in a))
def angle(a, b, c): return abs(math.degrees(math.atan2(*ldir(b, c)[::-1]) - math.atan2(*ldir(a, b)[::-1])))

cut = []
for i in range(len(path)-1):
  pdir = tuple(x // abs(x) if x != 0 else 0 for x in ldir(path[i], path[i+1]))
  print(i, path[i], path[i+1], pdir)
  if sum(pdir) == -1:
    cut.append(mul(path[i], scale(pdir, -1)[::-1]))
print(cut)

# PD = ((0, 0), (1, 0), (0, 1), (1, 1))
# PD = {
#   (0, 1): ((0, 1), (1, 1)),
#   (0, -1): ((0, 0), (1, 0)),
#   (1, 0): ((0, 0), (0, 1)),
#   (-1, 0): ((1, 0), (1, 1))
# }
# vertex = [(0, 0), (1, 0)]
# for i in range(1, len(path) - 1):
#   pdir = tuple(x // abs(x) if x != 0 else 0 for x in ldir(path[i+1], path[i]))
  # print(path[i+1], path[i], pdir)
  # points = [mov(p, dp) for p in path[i:i+2] for dp in PD[pdir]]
  # print(points)
  # while True:
  #   print(i, pdir, mov(vertex[-1], pdir), vertex, points)
  #   m = [(j, a, mag(ldir(vertex[-1], p))) for j, p in enumerate(points) if p not in vertex and (a := angle(mov(vertex[-1], pdir), vertex[-1], p)) % 90 == 0]
  #   ni = min(m, key=lambda x: x[1:])[0]
  #   vertex.append(points[ni])
  #   print(m, points[ni])
  #   print()
  #
  #   x, y = zip(*vertex)
  #   y = mul(y, -1)
  #   plt.figure()
  #   plt.plot(x, y, "or")
  #   plt.show()
  #
  #   if ni // 4 > 0: break
# print(vertex)



# points = sorted({ mov(p, dp) for p in path for dp in PD }, key=lambda x: (x[1], x[0]))
# print(points)
# print(len(points))

#
# m = [points[0], points[1]]
# vis = { 0 }
# while len(m) < 10:
#   src = ldir(m[-2], m[-1])
#   print(m[-2], m[-1])
#   tmp = list(filter(lambda x: x[1] % 90 == 0, ((j, angle(src, ldir(m[-1], points[j]))) for j in range(len(points)) if points[j] not in m)))
#   for j, a in sorted(tmp, key=lambda x: x[1]):
#     print(f"\t{points[j]} ({a})")
#   p = points[min(tmp, key=lambda x: x[1])[0]]
#   m.append(p)
# print(m)











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
