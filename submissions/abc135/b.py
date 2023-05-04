N = int(input())
pLst = list(map(int, input().split()))

ansCnt = 0
for i in range(N):
    if pLst[i] != (i + 1):
        ansCnt += 1

if ansCnt <= 2:
    print('YES')
else:
    print('NO')
