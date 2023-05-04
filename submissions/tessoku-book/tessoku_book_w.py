INF = 10 ** 18
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

dp = [[INF] * (1 << N) for _ in range(M + 1)]
dp[0][0] = 0

for i in range(1, M + 1):
    for j in range(1 << N):
        tmp = 0
        for k in range(N):
            if (j >> k) & 1 or A[i - 1][k]:
                tmp += (1 << k)

        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        dp[i][tmp] = min(dp[i][tmp], dp[i - 1][j] + 1)
if dp[M][(1 << N) - 1] == INF:
    print(-1)
else:
    print(dp[M][(1 << N) - 1])
