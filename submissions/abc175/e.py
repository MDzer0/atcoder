R, C, K = map(int, input().split())

dp = [[-1] * 4 for _ in range(C + 1)]
masu = [[0] * C for _ in range(R)]
for i in range(K):
    r, c, v = map(int, input().split())
    masu[r - 1][c - 1] = v

dp[0][0] = 0

for i in range(R):
    cdp = dp[:][:]
    for j in range(C):
        for k in reversed(range(3)):
            if dp[j][k] >= 0:
                dp[j][k + 1] = max(dp[j][k + 1], dp[j][k] + masu[i][j])

        for k in range(4):
            cdp[j][0] = max(dp[j][k], cdp[j][0])
            dp[j + 1][k] = max(dp[j][k], dp[j + 1][k])
    dp = cdp[:][:]

print(max(dp[C - 1]))
