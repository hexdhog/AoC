#!/usr/bin/env python3

from __future__ import annotations

import sys

from functools import reduce

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

def cycle():
  lcnt, hcnt = 1, 0
  upd = [mods["broadcaster"]]
  while len(upd) > 0:
    tmp = []
    for src in upd:
      lcnt, hcnt = lcnt+int(not src.state)*len(src.childs), hcnt+int(src.state)*len(src.childs)
      for d, s in zip(src.childs, (d.process(src) for d in src.childs)):
        if s is None: continue
        d.state = s
        tmp.append(d)
    upd = tmp
  return lcnt, hcnt

def snap(): return { name: mod.state for name, mod in mods.items() }

NCYCLES = 1000
org, i = snap(), 0
lcnt, hcnt = cycle()
while (i := i+1) < NCYCLES and snap() != org: lcnt, hcnt = (a+b for a, b in zip((lcnt, hcnt), cycle()))
lcnt, hcnt = lcnt*(NCYCLES//i), hcnt*(NCYCLES//i) # TODO: what if i is not a multiple of NCYCLES?
print(f"cycles: {i}; low: {lcnt}; high: {hcnt}; total: {lcnt*hcnt}")
