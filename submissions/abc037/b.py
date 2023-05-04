N, Q = map(int, input().split())
aLst = [list(map(int, input().split())) for i in range(Q)]
ansLst = [0] * N

for i in range(Q):
    for j in range(aLst[i][0] - 1, aLst[i][1]):
        ansLst[j] = aLst[i][2]

for i in ansLst:
    print(i)
