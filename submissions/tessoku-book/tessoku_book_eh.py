N, M = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b)
    g[b - 1].append(a)

ans = 0
tmp = 0
for i in range(N):
    if len(g[i]) > tmp:
        tmp = len(g[i])
        ans = i + 1
print(ans)
