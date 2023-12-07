#!/usr/bin/env python3

import sys

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def replace_first(src: str) -> str:
  for i in range(len(src)):
    for idx, d in enumerate(digits):
      if src[i:i+len(d)] == d: return src[0:i] + str(idx+1) + src[i+len(d):]
  return src

def replace_last(src: str) -> str:
  for i in range(len(src)-1, -1, -1):
    for idx, d in enumerate(digits):
      if src[max(i-len(d), 0)+1:i+1] == d: return src[0:max(i-len(d), 0)+1] + str(idx+1) + src[i+1:]
  return src

def replace(s: str) -> str:
  for i in range(len(s)):
    for idx, d in enumerate(digits):
      if s[i:i+len(d)] == d: return replace(s[0:i] + str(idx+1) + s[i+len(d):])
      if s[-i-len(d):-i if i != 0 else None] == d: return replace(s[:-i-len(d)] + str(idx+1) + (s[-i:] if i != 0 else ""))
  return s

data = [l.strip() for l in sys.stdin.readlines()]
print("##### METHOD 1 #####")
# print("\n".join(replace_first(x) for x in data), end="\n\n")
print("answer:", sum(x[0] * 10 + x[-1] for x in (tuple(map(int, filter(str.isdigit, replace_last(replace_first(x))))) for x in data)))
print()

print("##### METHOD 2 #####")
# print("\n".join(replace(x) for x in data), end="\n\n")
print("answer:", sum(x[0] * 10 + x[-1] for x in (tuple(map(int, filter(str.isdigit, replace(x)))) for x in data)))
