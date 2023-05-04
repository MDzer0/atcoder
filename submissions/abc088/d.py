import queue

def bfs(s1,s2):
    global ans
    queueX = queue.Queue()
    queueY = queue.Queue()
    queueX.put(s1)
    queueY.put(s2)
    s[s1][s2] = 0
    while queueX.empty() == False:
        x = queueX.get()
        y = queueY.get()

        for i in range(4):
            nextX = x + moveR[i]
            nextY = y + moveC[i]
            if 0 <= nextX and nextX < H\
                and 0 <= nextY and nextY < W\
                and s[nextX][nextY] != '#'\
                and s[nextX][nextY] == '.':
                s[nextX][nextY] = s[x][y] + 1
                queueX.put(nextX)
                queueY.put(nextY)

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
cnt = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            cnt += 1
moveR = [0, 1, -1, 0]
moveC = [1, 0, 0, -1]
bfs(0,0)
if s[H - 1][W - 1] == '.':
    print(-1)
else:
    print(H * W - cnt - s[H - 1][W - 1] - 1)
