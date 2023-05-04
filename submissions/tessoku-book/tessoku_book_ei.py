import sys
sys.setrecursionlimit(10 ** 7)

def dfs(v):
    check.append(v + 1)
    visit[v] = 1
    if v == N - 1:
        for i in check:
            print(i)
        exit()
    for i in g[v]:
        if visit[i] == 1: continue
        dfs(i)
        check.pop()

N, M = map(int, input().split())
check = []
visit = [0] * N
g = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dfs(0)
