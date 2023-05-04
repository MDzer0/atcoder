N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
grundy = [0] * 100001
for i in range(100001):
    transit = [False, False, False]
    if i >= X:
        transit[grundy[i - X]] = True
    if i >= Y:
        transit[grundy[i - Y]] = True

    if transit[0] == False:
        grundy[i] = 0
    elif transit[1] == False:
        grundy[i] = 1
    else:
        grundy[i] = 2

xor = 0
for i in range(N):
    xor ^= grundy[A[i]]
if xor != 0:
    print('First')
else:
    print('Second')
