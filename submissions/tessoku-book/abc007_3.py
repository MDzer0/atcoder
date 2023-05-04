from collections import deque

R, C = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
g = [list(input()) for _ in range(R)]
g[sx -1][sy - 1] = 0
X = [0, 1, -1, 0]
Y = [1, 0, 0, -1]
que = deque()
que.append((sx - 1, sy - 1))

while que:
    q = que.popleft()
    for i in range(4):
        nextX = X[i] + q[0]
        nextY = Y[i] + q[1]

        if 0 <= nextX and nextX < R\
            and 0 <= nextY and nextY < C\
            and g[nextX][nextY] == '.':
            g[nextX][nextY] = int(g[q[0]][q[1]]) + 1
            que.append((nextX, nextY))

            if nextX == gx - 1 and nextY == gy - 1:
                print(g[nextX][nextY])
                exit()
