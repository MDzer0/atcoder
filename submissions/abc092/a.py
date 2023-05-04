ryoKinLst = [0] * 4
for i in range(4):
    ryoKinLst[i] = int(input())

minA = 0
minC = 0

minA = min(ryoKinLst[0], ryoKinLst[1])
minC = min(ryoKinLst[2], ryoKinLst[3])

print(minA + minC)
