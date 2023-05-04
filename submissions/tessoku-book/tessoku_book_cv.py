import math

INF = 10 ** 19
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
jikan = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j: continue
        jikan[i][j] = math.sqrt((XY[i][0] - XY[j][0]) ** 2\
                                + (XY[i][1] - XY[j][1]) ** 2)

dp = [[INF] * N for _ in range(1 << N)]
dp[0][0] = 0
for i in range(1 << N):
    for j in range(N):
        for k in range(N):
            if i >> k & 1 == 0:
                dp[i + (1 << k)][k] = min(dp[i + (1 << k)][k],
                                          dp[i][j] + jikan[j][k])
print(dp[(1 << N) - 1][0])
