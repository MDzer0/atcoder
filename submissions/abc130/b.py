N, X = map(int,input().split())
lLst = list(map(int, input().split()))
D = 0
ansLst = []
ansLst.append(D)
tmp1 = 0
for i in range(N):
    tmp = tmp1 + lLst[i]
    if tmp <= X:
        ansLst.append(tmp)
        tmp1 = tmp
    else:
        break

print(len(ansLst))
