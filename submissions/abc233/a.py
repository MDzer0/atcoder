import math

X, Y = map(int, input().split())
if X >= Y:
    print(0)
else:
    ans = math.ceil((Y - X) / 10)
    print(ans)
