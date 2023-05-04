S = input()
ansLst = [0] * 6
sLst = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(6):
    if i != 5:
        print(S.count(sLst[i]), end=' ')
    else:
        print(S.count(sLst[i]))
