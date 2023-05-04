N = int(input())
S = input()
MOD = 10 ** 9 + 7
atlist = 'atcoder'
dp = [[0] * 8 for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(8):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        if j < 7 and S[i] == atlist[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

print(dp[N][7])
