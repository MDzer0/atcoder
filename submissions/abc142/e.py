INF = 10 ** 18
N, M = map(int, input().split())
dp = [[INF for _ in range(1 << N)] for _ in range(M + 1)]
cost = [0] * M
bit = [0] * M
for i in range(M):
    cost[i], b = map(int, input().split())
    c = list(map(int, input().split()))
    d = 0
    for j in range(len(c)):
        d |= 1 << (c[j] - 1)
    bit[i] = d

dp[0][0] = 0
for i in range(M):
    for j in range(1 << N):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        to = bit[i] | j
        dp[i + 1][to] = min(dp[i + 1][to], dp[i][j] + cost[i])

ans = dp[M][(1 << N) - 1]
if ans == INF:
    print(-1)
else:
    print(ans)
