import math
a, b, x = map(int, input().split())
t = a * a * b
tan = 0
if (x > t / 2):
    tan = math.atan(2 * ((a * a * b) - x) / (a * a * a))
else:
    tan = math.atan((a * b * b) / (2 * x))

ans = tan * 180 / math.pi

print(ans)
