N = int(input())
p = list(map(int, input().split()))

dp = [[0] * (10001) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(10001):
        if dp[i][j] != 0:
            dp[i + 1][j + p[i]] = 1
        if dp[i + 1][j] == 0:
            dp[i + 1][j] = dp[i][j]

print(dp[N].count(1))
