N, D = map(int, input().split())
ansB = True
iMinT = D + 1
iMaxT = iMinT + D
ansCnt = 1
while ansB:
    if N <= iMaxT:
        break

    iMinT = iMaxT + D + 1
    iMaxT = iMinT + D
    ansCnt += 1

print(ansCnt)
