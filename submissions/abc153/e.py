INF = 10 ** 9 + 7
H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
dp = [INF] * (H + 1)
dp[0] = 0

for i in range(N):
    for j in range(H):
        if dp[j] == INF: continue
        if j + ab[i][0] <= H:
            dp[j + ab[i][0]] = min(dp[j + ab[i][0]], dp[j] + ab[i][1])
        else:
            dp[H] = min(dp[H], dp[j] + ab[i][1])

print(dp[H])
