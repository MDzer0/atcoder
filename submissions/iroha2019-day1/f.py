import sys
N, K = map(int, input().split())
ansLst = []
tmp = N
ans = 0
for i in range(K - 1):
    for j in range(2, int(pow(N, 1 / 2)) + 1):
        if tmp % j == 0:
            tmp = int(tmp / j)
            ansLst.append(j)
            break
        if j == int(pow(N, 1 / 2)):
            print(-1)
            sys.exit()
    if tmp == 1:
        print(-1)
        sys.exit()

ansLst.append(tmp)
for i in range(len(ansLst) - 1):
    print(ansLst[i], end=' ')
print(ansLst[len(ansLst) - 1])
