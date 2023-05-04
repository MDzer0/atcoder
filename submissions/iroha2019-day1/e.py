N, A, B = map(int, input().split())
if B != 0:
    dLst = list(map(int, input().split()))
    dLst.sort()

    dans = N - len(dLst)
    if dLst[0] > A:
        dans -= int(dLst[0] / A)
    for i in range(1, B):
        tmp = dLst[i] - (dLst[i - 1] + 1)
        if tmp >= A:
            dans -= int(tmp / A)
    tmp = N - dLst[B - 1]
    if tmp >= A:
        dans -= int(tmp / A)
    print(dans)
else:
    print(0)
