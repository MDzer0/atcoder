MOD = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
    exit()

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
    dp[i][1] = dp[i - 1][0]

ans = 0
ans += A[0] * (dp[N - 1][0] + dp[N - 1][1])
ans += A[N - 1] * dp[N - 2][1]

for i in range(1, N - 1):
    l = i - 1
    r = N - i - 1
    ans += (A[i] * (dp[l][0] + dp[l][1]) * (dp[r][0] + dp[r][1])) % MOD
    ans %= MOD
    ans -= (A[i] * dp[l][0] * dp[r][0]) % MOD
    ans %= MOD

print(ans)
