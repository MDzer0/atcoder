a = input()
k = int(input())
sLst = [''] * (len(a) - k + 1)

for i in range(len(a) - k + 1):
    for j in range(i, k + i):
        sLst[i] = a[i:k + i]
ansSet = set(sLst)
print(len(ansSet))
