# pythonではpow(x, y, mod)で同様のことができるので
# 今後、実装は不要
def pow(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        ans = pow(x ** 2 % INF, y // 2)
    else:
        ans = (pow(x ** 2 % INF, y // 2) * x) % INF
    return ans

def comb_big(m, k):
    x, y = 1, 1
    for i in range(k):
        x = x * (m - i) % INF
        y = y * (k - i) % INF
    return x * pow(y, INF - 2) % INF

INF = 10 ** 9 + 7
n, a, b = map(int, input().split())

ans = pow(2, n) - 1 - comb_big(n, a) - comb_big(n, b)
print((ans + INF) % INF)
