mseList = [list(map(str, input().split())) for i in range(4)]
ansList = [['.' for i in range(4)] for j in range(4)]

for i in range(4):
    for j in range(4):
        ansList[-1 - i][-1 - j] = mseList[i][j]

for i in range(4):
    for j in range(4):
        print(ansList[i][j], end=' ')
    print('\r')
