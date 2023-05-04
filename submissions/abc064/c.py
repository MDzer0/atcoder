clst = [0, 0, 0, 0, 0, 0, 0, 0, 0]

N = int(input())
a = list(map(int, input().split()))

for i in a:
    if i <= 399:
        clst[0] += 1
    elif i <= 799:
        clst[1] += 1
    elif i <= 1199:
        clst[2] += 1
    elif i <= 1599:
        clst[3] += 1
    elif i <= 1999:
        clst[4] += 1
    elif i <= 2399:
        clst[5] += 1
    elif i <= 2799:
        clst[6] += 1
    elif i <= 3199:
        clst[7] += 1
    else:
        clst[8] += 1
minans = 0
maxans = 0

for i in range(9):
    if 0 < clst[i] and i != 8:
        minans += 1
    if i == 8 and minans == 0:
        minans += 1
maxans = minans + clst[8]

if sum(clst[:8]) == 0:
    maxans -= 1

print(minans, maxans)
