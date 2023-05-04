INF = 10 ** 9
N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [INF] * N
dp[0] = 0
for i in range(1, N):
    for j in range(K):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i - 1] + abs(h[i - 1] - h[i + j]))

print(dp[N - 1])
