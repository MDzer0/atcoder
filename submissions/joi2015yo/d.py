INF = 10 ** 9 + 7
N, M = map(int, input().split())
toshi = [int(input()) for _ in range(N)]
kuro = [int(input()) for _ in range(M)]
dp = [[INF] * (M + 1) for _ in range(N + 1)]
for i in range(M + 1):
    dp[0][i] = 0

for i in range(N):
    for j in range(M):
        dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j] + toshi[i] * kuro[j])

print(dp[N][M])
