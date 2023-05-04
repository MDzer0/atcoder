N, Ma, Mb = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(N)]
INF = 10 ** 9 + 7
dp = [[[INF] * (Mb * N + 1) for _ in range(N * Ma + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    for j in range(Ma * N + 1):
        for k in range(Mb * N + 1):
            if j - abc[i][0] >= 0 and k - abc[i][1] >=0:
                dp[i + 1][j][k] = min(dp[i][j - abc[i][0]][k - abc[i][1]] + abc[i][2], dp[i][j][k])
            else:
                dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])

ans = INF
for i in range(1, Ma * N + 1):
    for j in range(1, Mb * N + 1):
        if Ma * j == Mb * i:
            ans = min(ans, dp[N][i][j])

print(ans if ans != INF else -1)
