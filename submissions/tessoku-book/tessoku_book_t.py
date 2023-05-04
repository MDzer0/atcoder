S = input()
T = input()
lenS = len(S)
lenT = len(T)
dp = [[0] * (lenS + 1) for _ in range(lenT + 1)]

for i in range(1, lenT + 1):
    for j in range(1, lenS + 1):
        if S[j - 1] == T[i - 1]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[lenT][lenS])
