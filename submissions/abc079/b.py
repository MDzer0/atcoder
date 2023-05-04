N = int(input())

lLst = [0] * (N + 1)

if N == 0:
    print(2)
elif N == 1:
    print(1)
else:
    lLst[0] = 2
    lLst[1] = 1
    for i in range(2, N + 1):
        lLst[i] = lLst[i - 1] + lLst[i - 2]

    print(lLst[N])
