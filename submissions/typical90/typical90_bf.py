MOD = 10 ** 5
N, K = map(int, input().split())
dp = [[0] * (MOD + 1) for _ in range(61)]

for i in range(1, MOD + 1):
    dp[0][i] = (i + (sum(map(int, str(i))))) % MOD

for i in range(1, 61):
    for j in range(1, MOD + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

ans = N
for i in range(61):
    if K >> i & 1:
        ans = dp[i][ans]
print(ans)
