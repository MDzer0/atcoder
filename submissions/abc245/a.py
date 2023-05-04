import sys
input = sys.stdin.readline

A, B, C, D = input().split()

if A < C:
  print("Takahashi")
elif A == C and B <= D:
  print("Takahashi")
else:
  print("Aoki")
