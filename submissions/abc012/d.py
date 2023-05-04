def warshallFloyd():
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
    return

N, M = map(int, input().split())
dp = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(M):
    a, b, t = map(int, input().split())
    dp[a - 1][b - 1] = t
    dp[b - 1][a - 1] = t

warshallFloyd()
ans = 10 ** 18
for i in range(N):
    ans = min(ans, max(dp[i]))

print(ans)
