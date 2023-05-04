N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(31)]
dp1 = [[0] * (N + 1) for _ in range(31)]
dp2 = [[0] * (N + 1) for _ in range(31)]
for i in range(1, N + 1):
    dp[0][i] = P[i - 1]
    dp1[0][i] = C[P[i - 1] - 1]
    dp2[0][i] = C[P[i - 1] - 1]

for i in range(1, 31):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]
        dp1[i][j] = dp1[i - 1][j] + dp1[i - 1][dp[i - 1][j]]
        dp2[i][j] = max(dp2[i - 1][j], dp1[i - 1][j] + dp2[i - 1][dp[i - 1][j]])

ans = -10 ** 18

for i in range(1, N + 1):
    index = i
    ansTmp = 0
    for j in range(31):
        if K >> j & 1:
            ans = max(ans, ansTmp + dp2[j][index])
            ansTmp += dp1[j][index]
            index = dp[j][index]

print(ans)
