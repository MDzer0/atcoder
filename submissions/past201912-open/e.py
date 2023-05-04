N, Q = map(int, input().split())
flst = [list(map(int, input().split())) for _ in range(Q)]
slst = [list('N' for i in range(N)) for _ in range(N)]
for i in range(Q):
    if flst[i][0] == 1:
        slst[flst[i][1] - 1][flst[i][2] - 1] = 'Y'
    elif flst[i][0] == 2:
        for j in range(N):
            if flst[i][1] != j + 1:
                if slst[j][flst[i][1] - 1] == 'Y':
                    slst[flst[i][1] - 1][j] = 'Y'

    else:
        tmp = []
        for j in range(N):
            if slst[flst[i][1] - 1][j] == 'Y':
                tmp.append(j)
        for j in range(len(tmp)):
                for k in range(N):
                    if flst[i][1] == k + 1:
                        continue
                    if slst[tmp[j]][k] == 'Y':
                        slst[flst[i][1] - 1][k] = 'Y'

for i in range(N):
    print(''.join(slst[i]))
