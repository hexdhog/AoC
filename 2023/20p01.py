#!/usr/bin/env python3

from __future__ import annotations

import sys

class Module:
  def __init__(self, mtype: str, childs: list, parents: list): self.mtype, self.childs, self.parents, self.state = mtype, childs, parents, mtype == "&"
  def process(self) -> None | bool:
    if self.mtype == "%": return None if any(p.state for p in self.parents) else not self.state
    if self.mtype == "&": return not all(p.state for p in self.parents)
    return self.state

mods = {}
for l in sys.stdin.readlines():
  a, b = l.strip().split(" ", 1)
  name, mtyp = a if (bcst := a == "broadcaster") else a[1:], a if bcst else a[0]
  mods[name] = Module(mtyp, b[3:].split(", "), [])

for mod in mods.values():
  for child in mod.childs:
    if child in mods: mods[child].parents.append(mod)

def cycle():
  lcnt, hcnt = 1, 0
  upd = ["broadcaster"]
  while len(upd) > 0:
    tmp = []
    for n, m, s in zip(upd, modl := [mods[n] for n in upd if n in mods], [m.process() for m in modl]):
      if s is None: continue
      lcnt, hcnt = lcnt+int(not s)*len(m.childs), hcnt+int(s)*len(m.childs)
      m.state = s
      for child in m.childs:
        tmp.append(child)
        print(f"{n} -{'high' if m.state else 'low'}-> {child}")
    upd = tmp
  print()
  return lcnt, hcnt

def snap(): return { name: mod.state for name, mod in mods.items() }

org, i = snap(), 1
print(org)
lcnt, hcnt = cycle()
print(snap())
cycle()
print(snap())
# print(lcnt, hcnt)
# while snap() != org:
#   l, h = cycle()
#   print(l, h)
#   lcnt, hcnt, i = lcnt+l, hcnt+h, i+1
#
# lcnt = lcnt * (1000//i)
# hcnt = hcnt * (1000//i)
# print(lcnt, hcnt)
