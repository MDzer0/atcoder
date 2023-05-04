from collections import deque

INF = 10 ** 10
H, W = map(int, input().split())
C1, C2 = map(int, input().split())
D1, D2 = map(int, input().split())

s = [list(input()) for _ in range(H)]
dist = [[INF] * W for _ in range(H)]

moveH = [0, 1, -1, 0]
moveW = [1, 0, 0, -1]

que = deque()
dist[C1- 1][C2 - 1] = 0
que.append((C1 - 1, C2 - 1))

while que:
    q = que.popleft()
    for i in range(4):
        nextx = q[0] + moveH[i]
        nexty = q[1] + moveW[i]

        if 0 <= nextx and nextx < H\
            and 0 <= nexty and nexty < W:
            if s[nextx][nexty] != '#':
                if dist[nextx][nexty] > dist[q[0]][q[1]]:
                    dist[nextx][nexty] = dist[q[0]][q[1]]
                    que.appendleft((nextx, nexty))
            else:
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        if i == 0 and j == 0: continue

                        if 0 <= q[0] + i and q[0] + i < H\
                            and 0 <= q[1] + j and q[1] + j < W\
                            and s[q[0] + i][q[1] + j] != '#':

                            if dist[q[0] + i][q[1] + j] > dist[q[0]][q[1]] + 1:
                                dist[q[0] + i][q[1] + j] = dist[q[0]][q[1]] + 1
                                que.append((q[0] + i, q[1] + j))

print(dist[D1 - 1][D2 - 1] if dist[D1 - 1][D2 - 1] != INF else -1)
