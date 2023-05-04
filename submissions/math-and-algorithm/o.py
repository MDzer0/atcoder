import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v):
    for i in g[v]:
        if i == v: continue
        if color[i] != -1: continue
        color[i] = (color[v] + 1) % 2
        dfs(i)
    return

N, M = map(int, input().split())
g = [[] for _ in range(N)]
color = [-1] * N
A = [0] * M
B = [0] * M

for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
    g[A[i]].append(B[i])
    g[B[i]].append(A[i])

for i in range(N):
    if color[i] == -1:
        color[i] = 0
        dfs(i)

for i in range(M):
    if color[A[i]] == color[B[i]]:
        print('No')
        exit()

print('Yes')
