N, L = map(int, input().split())
x = list(map(int, input().split()))
T = list(map(int, input().split()))
INF = 10 ** 19
dp = [INF] * (L + 1)
shogai = [0] * (L + 1)
for i in x:
    shogai[i] = -1

dp[0] = 0

for i in range(1, L + 1):
    if shogai[i] != -1:
        if shogai[i - 1] != -1:
            dp[i] = min(dp[i], dp[i - 1] + T[0])
    if i >= 2:
        if shogai[i] == -1:
            dp[i] = min(dp[i], dp[i - 2] + T[1] + T[0] + T[2])
        else:
            dp[i] = min(dp[i], dp[i - 2] + T[1] + T[0])
    if i >= 4:
        if shogai[i] == -1:
            dp[i] = min(dp[i], dp[i - 4] + (3 * T[1]) + T[0] + T[2])
        else:
            dp[i] = min(dp[i], dp[i - 4] + (3 * T[1]) + T[0])
    if shogai[i] == -1:
        dp[i] = min(dp[i], dp[i - 1] + T[2] + T[0])
        shogai[i] = 0

ans = dp[L]
jnp = [2.5, 1.5, 0.5]
for i in range(3):
    ans = min(ans, dp[L - 3 + i] + (0.5 * T[0] + jnp[i] * T[1]))

print(int(ans))
