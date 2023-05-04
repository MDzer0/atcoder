import math

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, x1

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

T = int(input())
for i in range(T):
    N, S, K = map(int, input().split())
    tmp = math.gcd(N, math.gcd(S, K))
    N //= tmp
    S //= tmp
    K //= tmp
    cnt = modinv(K, N)
    if cnt == -1:
        print(-1)
    else:
        print(cnt * (-S) % N)
