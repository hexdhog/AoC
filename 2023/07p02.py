#!/usr/bin/env python3

from __future__ import annotations

import sys

table = [(x[0], int(x[1])) for x in [l.split() for l in sys.stdin.readlines()]]

class Hand:
  CARDS = "J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"
  def __init__(self, hand: str, bid: int) -> None:
    self.hand, self.bid, self.value = hand, bid, tuple(self.CARDS.index(x) for x in hand)
    joker = set(self.CARDS[-1]*len(self.hand) if all(x == "J" for x in hand) else hand.replace("J", ""))
    hand = hand.replace("J", max(((x, hand.count(x)) for x in joker), key=lambda x: x[1])[0])
    self.htype = tuple(sorted((hand.count(x) for x in set(hand)), reverse=True))
  def __lt__(self, other: Hand) -> bool: return self.htype == other.htype and self.value < other.value or self.htype < other.htype

print(sum([(i+1)*h.bid for i, h in enumerate(sorted([Hand(*x) for x in table]))]))
