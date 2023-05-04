import sys
sys.setrecursionlimit(10**6)

def dfs(v, n):
    check[v] = 1
    for i in g[v]:
        if i == n: continue
        if check[i] != 1:
            dfs(i, v)
    return

N, M = map(int, input().split())
g = [[] for _ in range(N)]
check = [0] * N

for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dfs(0, 0)
for i in range(N):
    if check[i] == 0:
        print('The graph is not connected.')
        exit()
print('The graph is connected.')
