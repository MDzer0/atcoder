from scipy.sparse.csgraph import floyd_warshall

INF = 10 ** 9 + 7
N = int(input())
a, b = map(int, input().split())
M = int(input())
dp = [[INF for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    dp[x][y] = 1
    dp[y][x] = 1
wf = floyd_warshall(dp)

d = [0] * N
d[a - 1] = 1
endcnt = int(wf[a - 1][b - 1])

for i in range(0, endcnt + 1):
    for j in range(N):
        if wf[a - 1][j] != i:
            continue
        for k in range(N):
            if wf[a - 1][k] == i + 1 and wf[j][k] == 1:
                d[k] += d[j]
                d[k] %= INF

print(d[b - 1])
