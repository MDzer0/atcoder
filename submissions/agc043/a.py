INF = 10 ** 9
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
dp = [[INF for _ in range(W)] for _ in range(H)]
if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(H):
    for j in range(W):
        if j != 0:
            cnt = 0
            if s[i][j] == '#' and s[i][j - 1] == '.':
                cnt += 1
            dp[i][j] = min(dp[i][j], dp[i][j - 1] + cnt)

        if i != 0:
            cnt = 0
            if s[i][j] == '#' and s[i - 1][j] == '.':
                cnt += 1
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + cnt)

print(dp[-1][-1])
