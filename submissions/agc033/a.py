from collections import deque

def bfs():
    while len(que) != 0:
        p = que.popleft()
        for i in range(4):
            nextX = p[0] + moveR[i]
            nextY = p[1] + moveC[i]
            if 0 <= nextX and nextX < H\
                and 0 <= nextY and nextY < W\
                and s[nextX][nextY] != '#'\
                and s[nextX][nextY] == '.':
                s[nextX][nextY] = s[p[0]][p[1]] + 1
                que.append([nextX, nextY])

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
moveR = [0, 1, -1, 0]
moveC = [1, 0, 0, -1]

que = deque()
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            que.append([i, j])
            s[i][j] = 0
bfs()
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, s[i][j])
print(ans)
