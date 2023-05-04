def warshallFloyd():
    for i in range(N):
        for j in range(N):
            if dp[j][i] == INF: continue
            for k in range(N):
                if dp[i][k] == INF: continue
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
    return


INF = 10 ** 18
N, M = map(int, input().split())
dp = [[INF] * N for _ in range(N)]
fist = [INF] * N
for i in range(N):
    dp[i][i] = 0

for i in range(M):
    u, v, l = map(int, input().split())
    if u == 1:
       fist[v - 1] = l
    elif v == 1:
        fist[u - 1] = l
    else:
        dp[u - 1][v - 1] = l
        dp[v - 1][u - 1] = l

warshallFloyd()
ans = 10 ** 10
for i in range(1, N - 1):
    for j in range(i + 1, N):
        ans = min(ans, fist[i] + fist[j] + dp[i][j])

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
