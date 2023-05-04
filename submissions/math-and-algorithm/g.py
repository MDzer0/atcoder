import math

N, X, Y = map(int, input().split())
ans = N // X
ans += N // Y
ans -= N // (X * Y // math.gcd(X, Y))
print(ans)
