X, Y, Z, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

tmpList = []
for i in range(X):
    for j in range(Y):
        tmpList.append(a[i] + b[j])

tmpList.sort(reverse=True)
ansLst = []
for i in range(min(K, len(tmpList))):
    for j in c:
        ansLst.append(tmpList[i] + j)

ansLst.sort(reverse=True)

for i in range(K):
    print(ansLst[i])
