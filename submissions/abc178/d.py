S = int(input())
INF = 10 ** 9 + 7
dp = [0] * (S + 1)
dp[0] = 1

for i in range(1, S + 1):
    for j in range(i - 2):
        dp[i] += dp[j]
        dp[i] %= INF

print(dp[S])
