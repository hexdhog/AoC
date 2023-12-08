#!/usr/bin/env python3

from __future__ import annotations

import sys
import queue
from functools import reduce
from multiprocessing import Process, Queue

def resolve(table: list, value: int) -> int:
  for dst, src, length in table:
    if src <= value <= src + length: return value + dst - src
  return value

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

def job(tasks: Queue, done: Queue) -> bool:
  while True:
    try:
      tables, start, length = tasks.get_nowait()
    except queue.Empty:
      break
    res = None
    for seed in range(start, start+length+1):
      tmp = reduce(lambda v, t: resolve(t, v), [seed, *tables])
      res = min(res, tmp) if isinstance(res, int) else tmp
    done.put(res)
  return True

if __name__ == "__main__":
  tmp = list(map(int, sys.stdin.readline().strip().split(":")[-1].split()))
  seed_ranges = [tuple(tmp[i:i+2]) for i in range(0, len(tmp), 2)]
  tables = [[tuple(map(int, y.split())) for y in x[1:]] for x in split([x.strip() for x in sys.stdin.readlines()], "")]
  tasks, done = Queue(), Queue() # type: ignore[var-annotated]
  for i in range(len(seed_ranges)): tasks.put((tables, *seed_ranges[i]))
  procs = []
  try:
    for _ in range(8):
      p = Process(target=job, args=(tasks, done))
      procs.append(p)
      p.start()

    for p in procs: p.join()

    res = []
    while not done.empty(): res.append(done.get())
    if len(res) > 0:
      print("results:", res)
      print("min:", min(res))
    else:
      print("results empty")
  except KeyboardInterrupt:
    print("execution stopped by user, killing processes")
    for p in procs: p.kill()
