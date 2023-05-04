import sys
sys.setrecursionlimit(10**9)

def dfs(x, y):
    if dp[x][y] != 0: return dp[x][y]
    nextx = [1, 0, -1, 0]
    nexty = [0, -1, 0, 1]
    cnt = 1
    for i in range(4):
        nx = x + nextx[i]
        ny = y + nexty[i]
        if 0 <= nx and nx < H and 0 <= ny and ny < W:
            if a[x][y] < a[nx][ny]:
                cnt += dfs(nx, ny)
                cnt %= INF
    dp[x][y] = cnt
    return cnt

INF = 10 ** 9 + 7
H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
dp = [[0 for _ in range(W)] for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        dfs(i, j)
        ans += dp[i][j]
        ans %= INF

print(ans)
