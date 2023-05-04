import bisect

N = int(input())
aList = [0] * N
for i in range(N):
    aList[i] = int(input())

maxTmp = max(aList)
tmpList = sorted(aList, reverse=True)
max2Tmp = tmpList[1]
maxCnt = aList.count(maxTmp)
ansList = [0] * N

for i in range(N):
    if aList[i] == maxTmp:
        if maxCnt > 1:
            for j in range(N):
                ansList[j] = maxTmp
            break
        else:
            ansList[i] = max2Tmp

    else:
        ansList[i] = maxTmp

for i in ansList:
    print(i)
