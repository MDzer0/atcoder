import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    for i in ki[n]:
        if ans[i[0]] != 0: continue
        if ans[n] != i[1]:
            ans[i[0]] = i[1]
        else:
            ans[i[0]] = (i[1] + 1) % N
        dfs(i[0])
    return

N, M = map(int, input().split())
ki = [[] for _ in range(N)]
ans = [0] * N
cnt = 0
for i in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    ki[u].append((v, c))
    ki[v].append((u, c))

dfs(0)
for i in ans:
    print(i)
