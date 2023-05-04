S = input()
T = input()
lenS = len(S)
lenT = len(T)
dp = [[0] * (lenS + 1) for _ in range(lenT + 1)]

for i in range(len(S) + 1):
    dp[0][i] = i
for i in range(1, len(T) + 1):
    dp[i][0] = i

for i in range(1, lenT + 1):
    for j in range(1, lenS + 1):
        tmp = dp[i - 1][j - 1]
        if S[j - 1] != T[i - 1]:
            tmp += 1
        dp[i][j] = min(tmp, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

print(dp[-1][-1])
