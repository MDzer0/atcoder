S = input()
dp = [[0] * (len(S) + 1) for _ in range(18)]
for i in range(1, len(S) + 1):
    if S[i - 1] == 'R':
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

for i in range(1, 18):
    for j in range(1, len(S) + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

ans = [0] * (len(S) + 1)
for i in range(1, len(S) + 1):
    ans[dp[17][i]] += 1
print(*ans[1:])
