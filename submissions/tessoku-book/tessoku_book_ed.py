N, K = map(int, input().split())
keta = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(len(str(i))):
        keta[i] += int(str(i)[j])

dp = [[0] * (N + 1) for _ in range(30)]
for i in range(1, N + 1):
    dp[0][i] = i - keta[i]

for i in range(1, 30):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

for i in range(1, N + 1):
    ans = i
    for j in reversed(range(30)):
        if K >> j & 1:
            ans = dp[j][ans]
    print(ans)
