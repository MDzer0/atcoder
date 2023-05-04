import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,Q = map(int,input().split())
aLst = [[int(x) for x in input().split()] for _ in range(N-1)]
pLst = [[int(x) for x in input().split()] for _ in range(Q)]

tmpLst = [[] for _ in range(N+1)]
for i, j in aLst:
    tmpLst[i].append(j)
    tmpLst[j].append(i)

ansLst = [0] * (N + 1)
for i,j in pLst:
    ansLst[i] += j

def dfs(v, p):
    for i in tmpLst[v]:
        if i == p:
            continue
        ansLst[i] += ansLst[v]
        dfs(i, v)


dfs(1, 0)

ans = ' '.join(map(str, ansLst[1:]))
print(ans)
