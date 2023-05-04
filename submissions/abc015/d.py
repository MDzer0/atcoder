f=lambda:map(int,input().split())
W = int(input())
N, K = f()
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = f()

dp = [[[0] * (W + 1) for _ in range(K + 1)] for _ in range(2)]

for i in range(N):
    index = i
    i = i % 2
    for j in range(K):
        for k in range(W + 1):
            if k - a[index] >= 0:
                dp[(i + 1) % 2][j + 1][k] = max(dp[i][j][k], dp[i][j][k - a[index]] + b[index], dp[i][j + 1][k])
            else:
                dp[(i + 1) % 2][j + 1][k] = max(dp[i][j][k], dp[i][j + 1][k])


print(dp[N % 2][K][W])
