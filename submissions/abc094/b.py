N, M, X = map(int, input().split())
sList = list(map(int, input().split()))

lCnt = 0
rCnt = 0
for i in sList:
    if X < i:
        lCnt += 1
    elif X > i:
        rCnt += 1

ans = min(lCnt, rCnt)
print(ans)
