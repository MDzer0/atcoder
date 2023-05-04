INF = 10 ** 9
N = int(input())
S = [list(input()) for _ in range(5)]
dp = [[INF for _ in range(3)] for _ in range(N + 1)]

dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, N + 1):
    bcnt = 0
    wcnt = 0
    rcnt = 0
    for j in range(5):
        if S[j][i - 1] == 'R':
            rcnt += 1
        elif S[j][i - 1] == 'B':
            bcnt += 1
        elif S[j][i - 1] == 'W':
            wcnt += 1
    dp[i][0] = min(dp[i - 1][1] + 5 - rcnt, dp[i - 1][2] + 5 - rcnt)
    dp[i][1] = min(dp[i - 1][0] + 5 - bcnt, dp[i - 1][2] + 5 - bcnt)
    dp[i][2] = min(dp[i - 1][0] + 5 - wcnt, dp[i - 1][1] + 5 - wcnt)

print(min(dp[N]))
