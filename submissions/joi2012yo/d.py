INF = 10 ** 4
N, K = map(int, input().split())
ab = [0] * (N + 1)
for i in range(K):
    a, b = map(int, input().split())
    ab[a] = b

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(3):
        for k in range(3):
            menu = [1, 2, 3]
            if ab[i + 1] != 0:
                menu = [ab[i + 1]]
            for l in menu:
                if i >= 2 and j == k  and k == l - 1: continue
                dp[i + 1][k][l - 1] += dp[i][j][k]
                dp[i + 1][k][l - 1] %= INF

ans = 0
for i in range(3):
    for j in range(3):
        ans += dp[N][i][j]
        ans %= INF
print(ans)
