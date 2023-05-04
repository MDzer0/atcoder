INF = 10 ** 18
N = int(input())
cost = [[0] * N for _ in range(N)]
toshi = [[0] * 3 for _ in range(N)]
dp = [[INF] * N for _ in range(1 << N)]

for i in range(N):
    x, y, z = map(int, input().split())
    toshi[i] = x, y, z

for i in range(N):
    for j in range(N):
        if i == j: continue
        cost[i][j] = abs(toshi[i][0] - toshi[j][0]) + \
                     abs(toshi[i][1] - toshi[j][1]) + max(0, toshi[j][2] - toshi[i][2])

dp[0][0] = 0
for i in range(1 << N):
    for j in range(N):
        for k in range(N):
            if i & 1 << k == 0:
                if j != k: dp[i | 1 << k][k] = min(dp[i | 1 << k][k], dp[i][j] + cost[j][k])
print(dp[(1 << N) - 1][0])
