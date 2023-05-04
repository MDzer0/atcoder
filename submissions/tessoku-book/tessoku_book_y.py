H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
dp = [[0] * (W + 2) for _ in range(H + 1)]
dp[1][1] = 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if c[i - 1][j - 1] != '#':
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
print(dp[H][W])
