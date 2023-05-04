INF = 10 ** 18
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * (1000 * N + 1) for _ in range(N + 1)]

dp[0][0] = 0
for i in range(N):
    for j in range(1000 * N + 1):
        if j - wv[i][1] >= 0 and dp[i][j - wv[i][1]] + wv[i][0] <= W:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - wv[i][1]] + wv[i][0])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

for i in reversed(range(1000 * N + 1)):
    if dp[N][i] != INF:
        print(i)
        exit()
