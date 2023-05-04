MOD = 10 ** 5
n, m = map(int, input().split())
kyori = [int(input()) for _ in range(n - 1)]
a = [int(input()) for _ in range(m)]
rui = [0] * n
for i in range(n - 1):
    rui[i + 1] = rui[i] + kyori[i]

ans = 0
tmp = 0
for i in range(m):
    ans += abs(rui[tmp] - rui[tmp + a[i]]) % MOD
    tmp += a[i]

print(ans % MOD)
