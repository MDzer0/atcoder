S = input()
MOD = 10 ** 9 + 7
dp = [[0] * 9 for _ in range(len(S) + 1)]
chk = 'chokudai'

for i in range(len(S) + 1):
    dp[i][0] = 1

for i in range(len(S)):
    for j in range(8):
        if S[i] == chk[j]:
            dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]
        dp[i + 1][j + 1] %= MOD
print(dp[len(S)][8])
