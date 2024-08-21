#!/usr/bin/env python3

from __future__ import annotations

import sys

from functools import reduce
from collections import deque

class Module:
  def __init__(self, name: str, mtype: str, childs: list, parents: list):
    self.name, self.mtype, self.childs, self.parents, self.state = name, mtype, childs, parents, False
  def init(self): self.state = self.mtype == "&" and not all(p.state for p in self.parents)
  def process(self, src: Module) -> None | bool:
    if self.mtype == "%": return not self.state if not src.state else None
    if self.mtype == "&": return not all(p.state for p in self.parents)
    return self.state

mods, childs = {}, {}
for l in sys.stdin.readlines():
  a, b = l.strip().split(" ", 1)
  name, mtyp = a if (bcst := a == "broadcaster") else a[1:], a if bcst else a[0]
  mods[name], childs[name] = Module(name, mtyp, [], []), b[3:].split(", ")
for m in set(reduce(lambda x, y: x+y, childs.values())): # type: ignore[operator]
  if m not in mods: mods[m], childs[m] = Module(m, "", [], []), []

for mod, chlds in ((mods[n], [mods[c] for c in childs[n]]) for n in mods):
  mod.childs = chlds
  for c in chlds: c.parents.append(mod)
for mod in mods.values(): mod.init()

def tree(root: str):
  q: deque = deque()
  q.append((mods[root], 0))
  vis = { n: False for n in mods }
  while len(q) > 0:
    m, l = q.pop()
    print(f"{'  '*l}{m.name}")
    vis[m.name] = True
    for c in m.parents:
      if not vis[c.name]: q.append((c, l+1))
  print([k for k in vis if not vis[k]])

tree("rx")

# def cycle(target: str, state: bool):
#   upd = [mods["broadcaster"]]
#   while len(upd) > 0:
#     tmp = []
#     for src in upd:
#       for c, s in zip(src.childs, (c.process(src) for c in src.childs)):
#         print(f"{src.name} -{'high' if src.state else 'low'}-> {c.name}")
#         if c.name == target and src.state == state: return True
#         if s is None: continue
#         c.state = s
#         tmp.append(c)
#     upd = tmp
#   return False
#
# i = 1
# while not cycle("rx", state=True): print(i := i+1)
# print(i)
