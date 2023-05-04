import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
d = [[] for _ in range(N)]
#ch = [0] * N
ans = 0

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)

def dfs(v, p, c):
    global ans
    if c == 2:
        if ch[v] == 0:
            ch[v] = 1
            ans += 1
        return

    for i in d[v]:
        if i == p:
            continue
        dfs(i, v, c + 1)
    return

for i in range(N):
    ch = [0] * N
    for j in d[i]:
        ch[j] = 1

    dfs(i, -1, 0)
    print(ans)
    ans = 0
