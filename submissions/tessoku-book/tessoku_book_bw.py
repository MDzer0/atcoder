N = int(input())
TD = [list(map(int, input().split())) for _ in range(N)]
TD.sort(key=lambda x: x[1])
dp = [[-1] * 1441 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(1441):
        if TD[i][1] < j or TD[i][0] > j:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - TD[i][0]] + 1)
print(max(dp[-1]))
