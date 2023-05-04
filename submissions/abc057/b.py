N, M = map(int, input().split())

abLst = [list(map(int, input().split())) for i in range(N)]
cdLst = [list(map(int, input().split())) for i in range(M)]

ansLst = [0] * N

for i in range(N):
    tmpMin = 100000000000
    ans = 0
    for j in range(M):
        tmp = abs(abLst[i][0] - cdLst[j][0]) + abs(abLst[i][1] - cdLst[j][1])
        if tmpMin > tmp:
            tmpMin = tmp
            ans = j + 1
    ansLst[i] = ans

for i in ansLst:
    print(i)
