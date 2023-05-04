R, C = map(int, input().split())
slist = [list(map(int, input().split())) for _ in range(R)]

cnt = 0
for i in range(R):
    cnt += slist[i].count(0)

ans = cnt
for i in range(2 ** R):
    copylist = [slist[_][:] for _ in range(R)]
    tmpcnt = cnt
    for j in range(R):
        if i >> j & 1:
            for k in range(C):
                if copylist[j][k] == 1:
                    copylist[j][k] = 0
                    tmpcnt += 1
                else:
                    copylist[j][k] = 1
                    tmpcnt -= 1
    for j in range(C):
        scnt = 0
        kcnt = 0
        for k in range(R):
            if copylist[k][j] == 1:
                kcnt += 1
            else:
                scnt += 1
        if kcnt > scnt:
            tmpcnt += kcnt - scnt
    ans = max(ans, tmpcnt)

print(ans)
