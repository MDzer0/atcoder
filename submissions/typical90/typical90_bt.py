import copy

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]
ans = 0
def dfs(h, w, cnt, gFlag):
    global ans
    cnt += 1
    if gFlag:
        if tmp[h][w] > 2:
            ans = max(ans, tmp[h][w])
        return

    for i in range(4):
        nx = h +x[i]
        ny = w + y[i]
        if nx > -1 and nx < H\
            and ny > -1 and ny < W and tmp[nx][ny] != '#':
            if tmp[nx][ny] == '.':
                tmp[nx][ny] = cnt
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = cnt
                gFlag = True
            else: continue
            dfs(nx, ny, cnt, gFlag)
            tmp[nx][ny] = '.'
            if gFlag:
                tmp[nx][ny] = 0
            gFlag = False
    return

for i in range(H):
    for j in range(W):
        gFlag = False
        tmp = copy.deepcopy(c)
        if tmp[i][j] == '#': continue
        tmp[i][j] = 0
        dfs(i, j, 0, gFlag)
if ans == 0:
    ans = -1
print(ans)
