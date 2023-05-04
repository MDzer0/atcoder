from collections import deque

INF = 10 ** 10
H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
dist = [[INF] * W for _ in range(H)]

moveH = [0, 1, -1, 0]
moveW = [1, 0, 0, -1]

sx, sy, gx, gy = 0, 0, 0, 0

for i in range(H):
    for j in range(W):
        if c[i][j] == 's':
            sx, sy = i, j
        if c[i][j] == 'g':
            gx, gy = i, j
que = deque()
dist[sx][sy] = 0
que.append((sx, sy))

while que:
    q = que.popleft()
    for i in range(4):
        nextx = q[0] + moveH[i]
        nexty = q[1] + moveW[i]

        if 0 <= nextx and nextx < H\
            and 0 <= nexty and nexty < W:
            if c[nextx][nexty] != '#':
                if dist[nextx][nexty] > dist[q[0]][q[1]]:
                    dist[nextx][nexty] = dist[q[0]][q[1]]
                    que.appendleft((nextx, nexty))
            else:
                if dist[nextx][nexty] > dist[q[0]][q[1]] + 1:
                    dist[nextx][nexty] = dist[q[0]][q[1]] + 1
                    que.append((nextx, nexty))

if dist[gx][gy] <= 2:
    print('YES')
else:
    print('NO')
