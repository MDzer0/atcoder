N, M = map(int, input().split())
kLst = [list(map(int, input().split())) for i in range(N)]

ansLst = [0] * M
for i in range(N):
    for j in range(1, len(kLst[i])):
        ansLst[kLst[i][j] - 1] += 1

ansCnt = 0
for i in ansLst:
    if i == N:
        ansCnt += 1

print(ansCnt)
