import math
X, Y, Z = map(int, input().split())
tmpx = Y / X
tmpy = Z * tmpx

if tmpy - int(tmpy) == 0:
    print(int(tmpy) - 1)
else:
    print(math.floor(tmpy))
