K, X = map(int, input().split())
ansLst = []
ansLst.append(X)
for i in range(1, K):
    ansLst.append(X - i)
    ansLst.append(X + i)

ansLst.sort()

for i in ansLst:
    print(i, end=' ')
