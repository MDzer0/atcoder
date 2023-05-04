import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for i in range(Q):
    E = int(input())
    x = math.sin((math.pi / 180) * (360 * E / T)) * -L / 2
    y = L / 2 - L / 2 * math.cos((math.pi / 180) * 360 * E / T)
    d = math.sqrt(X ** 2 + (x - Y) ** 2)
    ans = math.atan2(y, d)
    print(180 * ans / math.pi)
