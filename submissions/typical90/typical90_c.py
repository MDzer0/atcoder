import sys
sys.setrecursionlimit(10**6)


def dfs(o, v, cnt, dist):
    dist[v] = min(dist[v], cnt)
    for i in michi[v]:
        if o == i: continue
        dfs(v, i, cnt + 1, dist)
    return

N = int(input())
michi = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    michi[a - 1].append(b - 1)
    michi[b - 1].append(a - 1)

dist = [10 ** 10] * N
dist[0] = 0
for i in michi[0]:
    dfs(0, i, 1, dist)

index = 0
tmp = 0
for i in range(N):
    if tmp <= dist[i]:
        index = i
        tmp = dist[i]

dist2 = [10 ** 10] * N
dist2[index] = 0
for i in michi[index]:
    dfs(index, i, 1, dist2)

ans = 0
for i in dist2:
    ans = max(ans, i)

print(ans + 1)
