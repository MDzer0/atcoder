N, K = map(int, input().split())

h = list(int(input()) for _ in range(N))
sh = sorted(h, reverse=True)
ans = sh[0] - sh[K - 1]
for i in range(1, N - K + 1):
    if N < (i + K):
        break
    ans = min(ans, sh[i] - sh[i + K - 1])

print(ans)
