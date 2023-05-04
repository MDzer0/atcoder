import sys
sys.setrecursionlimit(10**6)

N = int(input())

def dfs(v, u, w):
    if w % 2 == 0:
        iro[v] = 0
    else:
        iro[v] = 1
    for i in ki[v]:
        if i[1] == u: continue
        dfs(i[1], v, w + i[0])
    return

ki = [[] for _ in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    ki[u].append((w, v))
    ki[v].append((w, u))

iro = [0] * N
dfs(0, 0, 0)
for i in iro:
    print(i)
