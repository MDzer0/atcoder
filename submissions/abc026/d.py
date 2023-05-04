from math import sin, pi

def f(t):
    return A * t + B * sin(C * pi * t)

A, B, C = map(int, input().split())
top = 1000
under = 0

while top - under > 10 ** (-12):
    mid = (top + under) / 2
    if f(mid) >= 100:
        top = mid
    else:
        under = mid

print(top)
