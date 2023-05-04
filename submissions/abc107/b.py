H, W = map(int, input().split())
a = [input() for _ in range(H)]
tmp = []
for i in range(H):
    cnt = a[i].count('.')
    if cnt == W: continue
    tmp.append(a[i])

delList = []
alen = len(tmp)
for i in range(W):
    dcnt = 0
    for j in range(alen):
        if tmp[j][i] == '.':
            dcnt += 1
    if dcnt == alen:
        delList.append(i)

ans = []
for i in range(alen):
    anstmp = ''
    for j in range(W):
        if not j in delList:
            anstmp += tmp[i][j]
    ans.append(anstmp)

for i in ans:
    print(i)
