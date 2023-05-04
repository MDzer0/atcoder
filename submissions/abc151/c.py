N, M = map(int, input().split())
p = [list(map(str, input().split())) for _ in range(M)]
aclst = [0] * (N + 1)
walst = [0] * (N + 1)
cntw = 0
cnta = 0
for i in range(M):
    if aclst[int(p[i][0])] == 0:
        if p[i][1] == 'WA':
            walst[int(p[i][0])] += 1
        else:
            cnta += 1
            cntw += walst[int(p[i][0])]
            aclst[int(p[i][0])] = 1


print(cnta, cntw)
