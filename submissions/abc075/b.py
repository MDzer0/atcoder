H, W = map(int, input().split())
sList = []
xList = [1, 1, 0, -1, -1, -1, 0, 1]
yList = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(H):
    sList.append(input())

for i in range(H):
    tmplist = list(sList[i])
    for j in range(W):
        if sList[i][j] == '#':
            continue

        tmpCnt = 0
        for k in range(8):
            tmpi = i + yList[k]
            tmpj = j + xList[k]
            if tmpi < 0 or tmpi >= H:
                continue
            if tmpj < 0 or tmpj >= W:
                continue
            if sList[tmpi][tmpj] == '#':
                tmpCnt += 1

        tmplist[j] = str(tmpCnt)
    print(''.join(tmplist))
