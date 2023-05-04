import math, cmath

N = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())

p0 = complex(x0, y0)
pn = complex(x1, y1)

o = (p0 + pn) / 2
r = cmath.rect(1, math.pi / 180 * 360 / N)
ans = (p0 - o) * r + o
print(ans.real, ans.imag)
