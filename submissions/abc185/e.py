N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(N + 1):
    dp[0][i] = i
for i in range(1, M + 1):
    dp[i][0] = i

for i in range(1, M + 1):
    for j in range(1, N + 1):
        tmp = dp[i - 1][j - 1]
        if A[j - 1] != B[i - 1]:
            tmp += 1
        dp[i][j] = min(tmp, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

print(dp[-1][-1])
