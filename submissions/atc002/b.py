def squaring(n, k, m):
    if k == 0:
        return 1
    if k % 2 == 0:
        tmp = squaring(n, k // 2, m)
        return tmp * tmp % m
    else:
        return squaring(n, k - 1, m) * n % m

N, M, P = map(int, input().split())
print(squaring(N, P, M))
