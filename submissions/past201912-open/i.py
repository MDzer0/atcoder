N, M = map(int, input().split())
INF = 10 ** 18
S = [0] * M
C = [0] * M
for i in range(M):
    tmp, C[i] = input().split()
    b = 0
    for j in range(N):
        if tmp[j] == 'Y':
            b |= 1 << j
    S[i] = b
dp = [[INF for _ in range(1 << N)] for _ in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    for j in range(1 << N):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        to = j | S[i]
        dp[i + 1][to] = min(dp[i + 1][to], dp[i][j] + int(C[i]))

ans = dp[M][(1 << N) - 1]
if ans == INF:
    print(-1)
else:
    print(ans)
