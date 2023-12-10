#!/usr/bin/env python3

from __future__ import annotations

import sys

table = [(x[0], int(x[1])) for x in [l.split() for l in sys.stdin.readlines()]]

class Hand:
  CARDS = "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"
  def __init__(self, hand: str, bid: int) -> None:
    self.hand, self.value, self.htype, self.bid = hand, tuple(self.CARDS.index(x) for x in hand), tuple(sorted((hand.count(x) for x in set(hand)), reverse=True)), bid
  def __repr__(self) -> str: return f"{self.hand} [type: {self.htype}; value: {self.value}; bid: {self.bid}]"
  def __lt__(self, other: Hand) -> bool: return self.htype == other.htype and self.value < other.value or self.htype < other.htype

print(sum([(i+1)*h.bid for i, h in enumerate(sorted([Hand(*x) for x in table]))]))
