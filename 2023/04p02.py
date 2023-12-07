#!/usr/bin/env python3

import sys

data = [l.strip() for l in sys.stdin.readlines()]
cards = {}
for card in data:
  c, n = card.split(":")
  w, h = (list(map(int, x.split())) for x in n.split("|"))
  cards[int(c.split()[-1])] = { "count": 1, "points": len([x for x in w if x in h]) }

for cn in cards:
  for i in range(1, cards[cn]["points"]+1): cards[cn+i]["count"] += cards[cn]["count"]

print(sum(cards[x]["count"] for x in cards))
