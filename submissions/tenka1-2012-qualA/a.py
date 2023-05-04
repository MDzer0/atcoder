n = int(input())
if n == 0 or n == 1:
    print(1)
    exit()
dp = [0] * n
dp[1] = 1

for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]
dp[0] = 1
print(sum(dp))
