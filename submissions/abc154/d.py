N, K = map(int, input().split())
p = list(map(int, input().split()))
rui = [0] * (N + 1)

for i in range(1, N + 1):
    rui[i] += rui[i - 1] + ((((p[i - 1] + 1) * p[i - 1]) // 2) / p[i - 1])

ans = rui[K]
for i in range(K, N + 1):
    ans = max(ans, rui[i] - rui[i - K])

print(ans)
