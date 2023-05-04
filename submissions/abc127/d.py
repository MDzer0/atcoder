N, M = map(int, input().split())
aLst = list(map(int, input().split()))
aLst.sort()
cdict = {}
for i in range(M):
    B, C = map(int, input().split())
    if C in cdict.keys():
        cdict[C] = cdict[C] + B
    else:
        cdict[C] = B

for i in aLst:
    if i in cdict.keys():
        cdict[i] = cdict[i] + 1
    else:
        cdict[i] = 1

sordC = sorted(cdict.items(), key=lambda x:x[0], reverse=True)
ans = 0
tmp = 0
for i in range(N):
    for j in range(sordC[i][1]):
        if tmp < N:
            ans += sordC[i][0]
            tmp += 1
        else:
            break
    if tmp >= N:
        break
print(ans)
