N, M, X, Y = map(int, input().split())
xLst = list(map(int, input().split()))
yLst = list(map(int, input().split()))

ans = 'War'
Z = []
for i in range(X + 1, Y + 1):
    Z.append(i)

delxLst = []
for i in range(len(Z)):
    for j in range(len(xLst)):
        if Z[i] <= xLst[j]:
            delxLst.append(i)
            break

delxLst.sort(reverse=True)
for i in range(len(delxLst)):
    del Z[delxLst[i]]

delyLst = []
for i in range(len(Z)):
    for j in range(len(yLst)):
        if Z[i] > yLst[j]:
            delyLst.append(i)
            break
delyLst.sort(reverse=True)
for i in range(len(delyLst)):
    del Z[delyLst[i]]

if len(Z) > 0:
    print('No War')
else:
    print('War')
