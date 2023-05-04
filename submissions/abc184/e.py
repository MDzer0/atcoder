import string
from collections import deque

def bfs2():
    while len(que) != 0:
        p = que.popleft()
        c = cost[p[0]][p[1]] + 1
        for i in range(4):
            nextX = p[0] + moveR[i]
            nextY = p[1] + moveC[i]
            if 0 <= nextX and nextX < H\
                and 0 <= nextY and nextY < W\
                and a[nextX][nextY] != '#':
                if cost[nextX][nextY] > c:
                    cost[nextX][nextY] = c
                    que.append((nextX, nextY))

        if str(a[p[0]][p[1]]).islower():
            index = string.ascii_lowercase.index(a[p[0]][p[1]])
            for j in warp[index]:
                if a[j[0]][j[1]] == string.ascii_lowercase[index]:
                    if cost[j[0]][j[1]] > c:
                        cost[j[0]][j[1]] = c
                        que.append(j)
            warp[index].clear()

INF = 10 ** 10
H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]
cost = [[INF] * W for _ in range(H)]
warp = [[] for _ in range(26)]

moveR = [0, 1, -1, 0]
moveC = [1, 0, 0, -1]
que = deque()
gx, gy = 0, 0
for i in range(H):
    for j in range(W):
        if a[i][j] == 'G':
            gx, gy = i, j
        elif a[i][j] == 'S':
            cost[i][j] = 0
            que.append((i, j))
            a[i][j] = 0
        elif a[i][j] != '#' and a[i][j] != '.':
            index = string.ascii_lowercase.index(a[i][j])
            warp[index].append((i, j))
bfs2()
if cost[gx][gy] == INF:
    print(-1)
else:
    print(cost[gx][gy])
