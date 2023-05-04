inList = []
startCnt = int(input())
goalCnt = 0
minLst = 1000000000000000
for i in range(5):
    A = int(input())
    inList.append(A)
    minLst = min(minLst, A)
ans = (-(-startCnt // minLst)) + 4
print(ans)
