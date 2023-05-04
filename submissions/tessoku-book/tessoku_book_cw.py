import bisect

N = int(input())
XY = []
for i in range(N):
    x, y = map(int, input().split())
    XY.append([x, -y])
XY.sort()
Y =[]

for i in range(N):
    Y.append(-XY[i][1])

LEN = 0
L = []
for i in range(N):
    pos = bisect.bisect_left(L, Y[i])
    if pos == LEN:
        L.append(Y[i])
        LEN += 1
    else:
        L[pos] = Y[i]

print(LEN)
