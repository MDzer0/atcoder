N, A, B, C = map(int, input().split())
lLst = [0] * N
for i in range(N):
    lLst[i] = int(input())
maxM = 10000

def dfs(nCnt, atake, btake, ctake):
    if nCnt == N:
        if min(atake, btake, ctake) > 0:
            return abs(A - atake) + abs(B - btake) + abs(C - ctake) - 30
        else:
            return maxM

    ret0 = dfs(nCnt + 1, atake, btake, ctake)
    ret1 = dfs(nCnt + 1, atake + lLst[nCnt], btake, ctake) + 10
    ret2 = dfs(nCnt + 1, atake, btake + lLst[nCnt], ctake) + 10
    ret3 = dfs(nCnt + 1, atake, btake, ctake + lLst[nCnt]) + 10
    return min(maxM, ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0))
