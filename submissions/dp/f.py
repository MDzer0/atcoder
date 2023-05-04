s = input()
t = input()
n = len(s)
m = len(t)
dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
cnt = dp[m][n]
ans = ''
while n > 0 and m > 0:
    if dp[m][n] == dp[m][n - 1]:
        n -= 1
    elif dp[m][n] == dp[m - 1][n]:
        m -= 1
    else:
        ans = s[n - 1] + ans
        n -= 1
        m -= 1

print(ans)
