inList = []
for i in range(5):
    inList.append(int(input()))
saigo = []
minCnt = 130
for i in inList:
    minx = int(i % 10)
    if minx != 0:
        minCnt = min(minCnt, minx)
    saigo.append(minx)
if minCnt == 130:
    minCnt = 0
minIdx = saigo.index(minCnt)
appx = inList.pop(minIdx)
inList.append(appx)
ans = 0
for i in range(len(inList)):
    ans += int(inList[i])
    if i != len(inList) - 1:
        amari = ans % 10
        if amari != 0:
            ans += + (10 - amari)

print(ans)
