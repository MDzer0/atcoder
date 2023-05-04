def dfs(x, y, cnt):
    global ans
    mn[x][y] = 0
    for i in range(4):
        nextX = x + moveR[i]
        nextY = y + moveC[i]
        if 0 <= nextX and nextX < m \
                and 0 <= nextY and nextY < n \
                and mn[nextX][nextY] == 1:
            mn[nextX][nextY] = 0
            dfs(nextX, nextY, cnt + 1)
    mn[x][y] = 1
    ans = max(ans, cnt)
    return

n = int(input())
m = int(input())
mn = [list(map(int, input().split())) for _ in range(m)]
moveR = [0, 1, -1, 0]
moveC = [1, 0, 0, -1]
ans = 0
for i in range(m):
    for j in range(n):
        if mn[i][j] == 1:
            tmp = dfs(i, j, 1)

print(ans)
