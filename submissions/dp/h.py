INF = 10 ** 9 + 7
H, W = map(int, input().split())
a = [input() for _ in range(H)]
dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if i + 1 < H and a[i + 1][j] == '.':
            dp[i + 1][j] = dp[i][j] + dp[i + 1][j]
            dp[i + 1][j] %= INF
        if j + 1 < W and a[i][j + 1] == '.':
            dp[i][j + 1] = dp[i][j + 1] + dp[i][j]
            dp[i][j + 1] %= INF

print(dp[H - 1][W - 1])
