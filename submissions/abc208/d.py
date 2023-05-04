def warshallFloyd():
    global ans
    for i in range(N):
        for j in range(N):
            for k in range(N):
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
                if dp[j][k] != INF:
                    ans += dp[j][k]
    return

INF = 10 ** 18
N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
ans = 0
for i in range(M):
    a, b, c = map(int, input().split())
    dp[a - 1][b - 1] = c

for i in range(N):
    dp[i][i] = 0

warshallFloyd()
print(ans)
