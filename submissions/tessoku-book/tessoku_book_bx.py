from bisect import bisect_left

MOD = 10 ** 9 + 7
N, W, L, R = map(int, input().split())
X = list(map(int, input().split()))
X = [0] + X + [W]
dp = [0] * (N + 2)
sumDp = [0] * (N + 2)

dp[0] = 1
sumDp[0] = 1

for i in range(1, N + 2):
    left = bisect_left(X, X[i] - R)
    right = bisect_left(X, X[i] - L + 1) - 1
    sum1 = 0
    sum2 = 0
    if left >= 1:
        sum1 = sumDp[left - 1]
    if right >= 0:
        sum2 = sumDp[right]

    dp[i] = sum2 - sum1
    dp[i] %= MOD
    sumDp[i] = sumDp[i - 1] + dp[i]
    sumDp[i] %= MOD

print(dp[N + 1])
