N = int(input())
PA = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in reversed(range(N - 1)):
    for l in range(N - i):
        r = l + i
        score1 = 0
        if l >= 1 and l <= PA[l - 1][0] - 1 <= r:
            score1 = PA[l - 1][1]

        score2 = 0
        if r <= N - 2 and l <= PA[r + 1][0] - 1 <= r:
            score2 = PA[r + 1][1]

        if l == 0: dp[l][r] = dp[l][r + 1] + score2
        elif r == N - 1: dp[l][r] = dp[l - 1][r] + score1
        else: dp[l][r] = max(dp[l][r + 1] + score2, dp[l - 1][r] + score1)

ans = 0
for i in range(N):
    ans = max(dp[i][i], ans)
print(ans)
