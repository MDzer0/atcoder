from collections import defaultdict

M = int(input())
mlist = [list(map(int, input().split())) for _ in range(M)]
N = int(input())
d = defaultdict(int)
for i in range(N):
    x, y = map(int, input().split())
    d[(x, y)] += 1

key = d.keys()
ansx = 0
ansy = 0
for j in key:
    aFlag = True
    tmpx = j[0] - mlist[0][0]
    tmpy = j[1] - mlist[0][1]
    for k in range(M):
        if (mlist[k][0] + tmpx, mlist[k][1] + tmpy) in d:
            continue
        else:
            aFlag = False
            break
    if aFlag:
        print(tmpx, tmpy)
        exit()
