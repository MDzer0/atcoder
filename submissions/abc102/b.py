N = int(input())
aLst = list(map(int, input().split()))

aLst.sort()
tmpMin = aLst[0]
tmpMax = aLst[N - 1]
ans = tmpMax - tmpMin
print(ans)
