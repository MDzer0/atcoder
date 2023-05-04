import math

INF = 10 ** 18
A, B = map(int, input().split())
tmp = math.gcd(A, B)
ans = (A * B) // tmp

if ans > INF:
    print('Large')
else:
    print(ans)
