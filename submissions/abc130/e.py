MOD = 10 ** 9 + 7

N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        if i - 1 >= 0 and j - 1 >= 0 and S[i - 1] == T[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] % MOD
        if i - 1 >= 0:
            dp[i][j] += dp[i - 1][j] % MOD
        if j - 1 >= 0:
            dp[i][j] += dp[i][j - 1] % MOD
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] -= dp[i - 1][j - 1] % MOD

print(dp[N][M] % MOD)
