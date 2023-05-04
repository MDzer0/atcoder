N = int(input())
dLst = [0] * N
for i in range(N):
    dLst[i] = int(input())

dLst.sort()
tmp = dLst[0]
ansCnt = 1
for i in range(1, N):
    if tmp < dLst[i]:
        ansCnt += 1
    tmp = dLst[i]

print(ansCnt)
