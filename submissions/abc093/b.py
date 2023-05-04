A, B, K = map(int, input().split())
tmp = [0] * K
for i in range(K):
    aTmp = A + i
    if B >= aTmp:
        print(aTmp)
        tmp[i] = aTmp

for i in range(K):
    bTmp = B - K + 1 + i
    if tmp.count(bTmp) == 0 and A <= bTmp:
        print(bTmp)
