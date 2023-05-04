N = int(input())
aLst = list(map(int, input().split()))

aLst.sort()

print(aLst[N - 1] - aLst[0])
