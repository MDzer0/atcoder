N = int(input())
sList = [['' for i in range(1)] for j in range(N)]

for i in range(N):
    sList[i] = input()

M = int(input())
tList = [['' for i in range(1)] for j in range(M)]
for i in range(M):
    tList[i] = input()

ansMax = 0
for i in sList:
    tmp = sList.count(i) - tList.count(i)
    ansMax = max(ansMax, tmp)

print(ansMax)
