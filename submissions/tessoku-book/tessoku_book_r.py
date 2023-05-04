N, S = map(int, input().split())
A = list(map(int, input().split()))
INF = S + 1
dp = [[0] * INF for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(INF):
        dp[i + 1][j] = dp[i][j]
        if j - A[i] >= 0 and dp[i][j - A[i]] == 1:
            dp[i + 1][j] = 1
if dp[N][S] == 1:
    print('Yes')
else:
    print('No')
