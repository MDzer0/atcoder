import math

N = int(input())
H = int(input())
W = int(input())

th = N - H + 1
tw = N - W + 1
print(th * tw)
