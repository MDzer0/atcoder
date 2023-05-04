N = int(input())
dp = [[0 for _ in range(3)] for _ in range(N + 1)]
a, b, c = map(int, input().split())
dp[1][0] = a
dp[1][1] = b
dp[1][2] = c
for i in range(2, N + 1):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i - 1][1] + a, dp[i - 1][2] + a)
    dp[i][1] = max(dp[i - 1][0] + b, dp[i - 1][2] + b)
    dp[i][2] = max(dp[i - 1][0] + c, dp[i - 1][1] + c)

print(max(dp[N]))
