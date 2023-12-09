#!/usr/bin/env python3

from __future__ import annotations

import sys
import queue
from multiprocessing import Process, Queue, current_process

def resolve(value: int | None, table: list) -> int | None:
  if value is None: return None
  for dst, src, size in table:
    if dst <= value < dst + size: return value + src - dst
  for _, src, size in table:
    if src <= value < src + size: return None
  return value

def job(tasks: Queue, done: Queue) -> bool:
  try:
    while True:
      tables, seed_ranges, start, length = tasks.get_nowait()
      print(f"{current_process().name} : {start} to {start+length}")
      for i in range(start, start+length):
        value: int | None = i
        for table in tables:
          value = resolve(value, table)
          if value is None: break
        if value is not None and any(s <= value < s+l for s, l in seed_ranges):
          done.put(i)
          break
  except queue.Empty:
    return True

def split(l: list, check: object) -> list:
  ret, tmp = [], [] # type: ignore[var-annotated]
  for e in l:
    if e == check:
      if len(tmp) > 0: ret.append(tmp)
      tmp = []
    else:
      tmp.append(e)
  ret.append(tmp)
  return ret

if __name__ == "__main__":
  tmp = list(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
  seed_ranges = [tuple(tmp[i:i+2]) for i in range(0, len(tmp), 2)]
  tables = [sorted([tuple(map(int, y.split())) for y in x[1:]], key=lambda x: x[0]) for x in reversed(split([x.strip() for x in sys.stdin.readlines()], ""))]
  dst, _, size = sorted(tables[0], key=lambda x: x[0]+x[2])[-1]

  MAX = dst + size
  PCOUNT = 8
  PSIZE = int(round(MAX / (PCOUNT * 2)))
  tasks, done = Queue(), Queue() # type: ignore[var-annotated]
  for r in [(i, i+PSIZE) for i in range(0, MAX, PSIZE)]: tasks.put((tables, seed_ranges, *r))
  procs = []
  try:
    for _ in range(PCOUNT):
      p = Process(target=job, args=(tasks, done))
      procs.append(p)
      p.start()

    while any(p.is_alive() for p in procs):
      for p in procs:
        if p.is_alive():
          p.join(timeout=1)
          if not p.is_alive(): print(p.name, "stopped")

    res = []
    while not done.empty(): res.append(done.get())
    if len(res) > 0: print("lowest location number:", min(res))
    else: print("no location found")
  except KeyboardInterrupt:
    print("execution stopped by user, killing processes")
    for p in procs: p.kill()
