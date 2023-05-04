N = int(input())
tList = list(map(int, input().split()))
M = int(input())
pLst = [list(map(int, input().split())) for i in range(M)]
ansLst = [0] * M

for i in range(M):
    tmp = 0
    for j in range(N):
        if j == (pLst[i][0] - 1):
            tmp += pLst[i][1]
        else:
            tmp += tList[j]

    ansLst[i] = tmp

for i in ansLst:
    print(i)
