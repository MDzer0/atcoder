import queue
import copy

def bfs(s1,s2):
    global ans
    cs = copy.deepcopy(s)
    queueX = queue.Queue()
    queueY = queue.Queue()
    queueX.put(s1)
    queueY.put(s2)
    cs[s1][s2] = 0
    while queueX.empty() == False:
        x = queueX.get()
        y = queueY.get()

        for i in range(4):
            nextX = x + moveR[i]
            nextY = y + moveC[i]
            if 0 <= nextX and nextX < H\
                and 0 <= nextY and nextY < W\
                and cs[nextX][nextY] != '#'\
                and cs[nextX][nextY] == '.':
                cs[nextX][nextY] = cs[x][y] + 1
                ans = max(ans, cs[nextX][nextY])
                queueX.put(nextX)
                queueY.put(nextY)

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

moveR = [0, 1, -1, 0]
moveC = [1, 0, 0, -1]
ans = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            bfs(i, j)

print(ans)
