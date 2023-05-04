def dfs(d):
    global ans
    if d == N:
        cntF = True
        for i in range(N):
            if slst[i] == 0:
                continue
            for j in range(N):
                if i == j or slst[j] == 0:
                    continue
                if g[i] == [] or g[i].count(j) == 0:
                    cntF = False
                    break
            if not cntF:
                break
        if cntF:
            ans = max(ans, slst.count(1))
        return
    for i in range(2):
        slst[d] = i
        dfs(d + 1)
    return

N, M = map(int, input().split())
g = [[] for _ in range(N)]
slst = [0] * N
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)
ans = 0
dfs(0)
print(ans)
