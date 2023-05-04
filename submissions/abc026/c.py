N = int(input())

bLst = [0] * (N - 1)
for i in range(N - 1):
    bLst[i] = int(input())
subLst = [[] for _ in range(N+1)]
for i in range(len(bLst)):
    subLst[bLst[i]].append(i + 2)

kLst = [0] * (N + 1)
for i in range(N, 0, -1):
    if subLst[i] == []:
        kLst[i] = 1
    elif len(subLst[i]) == 1:
        kLst[i] = 2 * (kLst[subLst[i][0]]) + 1
    else:
        bMax = 0
        bMin = 10000000000000000
        for j in range(len(subLst[i])):
            bMax = max(bMax, kLst[subLst[i][j]])
            bMin = min(bMin, kLst[subLst[i][j]])
        kLst[i] = bMax + bMin + 1

print(kLst[1])
