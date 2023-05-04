shima = [list(input()) for _ in range(10)]
chckLst = [[0] * 10 for _ in range(10)]
yoko = [1, -1, 0, 0]
tate = [0, 0, 1, -1]
cnt = 0
sx = -1
sy = -1
ans = 'NO'
def dfs(x, y):
    global ans
    global chckCnt
    for i in range(len(yoko)):
        if x + tate[i] >= 0 and x + tate[i] <= 9 and\
            y + yoko[i] >= 0 and y + yoko[i] <= 9:
            if shima[x + tate[i]][y + yoko[i]] == 'o' and chckLst[x + tate[i]][y + yoko[i]] != chckCnt:
                chckLst[x + tate[i]][y + yoko[i]] = chckCnt
                dfs(x + tate[i], y + yoko[i])
            else:
                continue
    return

for i in range(10):
    cnt += shima[i].count('o')
    if sx == -1:
        if 'o' in shima[i]:
            sx = i
            sy = shima[i].index('o')

chckCnt = 1
for i in range(10):
    for j in range(10):
        if shima[i][j] != 'o':
            shima[i][j] = 'o'
            chckLst[sx][sy] = chckCnt
            dfs(sx, sy)
            compCnt = 0
            for k in range(10):
                compCnt += chckLst[k].count(chckCnt)
            shima[i][j] = 'x'
            chckCnt += 1
        else:
            continue

        if compCnt == cnt + 1:
            ans = 'YES'
            break

print(ans)
