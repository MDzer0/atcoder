N = int(input())
sLst = list(input() for i in range(N))
ansList = [[''] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        ansList[i][N - 1 - j] = sLst[j][i]

for i in range(N):
    for j in range(N):
        print(ansList[i][j], end='')

    print('')
