N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(61)]
for i in range(1, N + 1):
    dp[0][i] = A[i - 1]

for i in range(1, 61):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]


ans = 1
for j in reversed(range(61)):
    if K >> j & 1:
        ans = dp[j][ans]
print(ans)
