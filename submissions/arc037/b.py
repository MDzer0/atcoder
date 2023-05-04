import sys
sys.setrecursionlimit(10**6)

def dfs(u, v):
    if chklst[u] == 1:
        return False
    chklst[u] = 1
    for i in d[u]:
        if i == v:
            continue
        if not dfs(i, u):
            return False
    return True


N, M = map(int, input().split())
d = [[] for _ in range(N)]
chklst = [0] * N
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    d[u].append(v)
    d[v].append(u)
cnt = 0
for i in range(N):
    if chklst[i] == 0:
        if dfs(i, i):
            cnt += 1

print(cnt)
