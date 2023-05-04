import sys
import numpy as np

readline = sys.stdin.readline

H, W, N = map(int, input().split())
hw = [list(map(int, readline().split())) for _ in range(H)]
dp = [[0] * W for _ in range(H)]

dp[0][0] = N - 1

for i in range(H):
    for j in range(W):
        tmp = dp[i][j]
        plus = ((tmp - 1) // 2 + 1)
        if hw[i][j] == 1:
            if j < W - 1:
                dp[i][j + 1] += plus
            if i < H - 1:
                dp[i + 1][j] += tmp - plus

        else:
            if i < H - 1:
                dp[i + 1][j] += plus
            if j < W - 1:
                dp[i][j + 1] += tmp - plus

dp = np.array(dp)
hw = np.array(hw)
dp = (dp + hw) % 2

x, y = 0, 0
for i in range(H):
    for j in range(y, W):
        if dp[i][j] == 1:
            y += 1
        if dp[i][j] == 0:
            x += 1
            break
    if y == W:
        break
    if x == H:
        break

print(x + 1, y + 1)
