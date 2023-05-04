from collections import defaultdict
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**6)

def dijkstra(s):
    used = [1] * N
    dp = [INF] * N
    dp[s] = 0
    hq = []
    used[s] = 0
    for i in cost[s]:
        heappush(hq, i)

    while hq:
        minv = heappop(hq)
        if used[minv[1]] == 0:
            continue
        v = minv[1]
        dp[v] = minv[0]
        used[v] = 0
        for i in cost[v]:
            if used[i[1]]:
                heappush(hq, [i[0] + dp[v], i[1]])
    return dp

def dfs(o, v, n):
    chk = 0
    if n != kyori[v]:
        return chk

    if de[C[v]] == 0:
        de[C[v]] += 1
        ans.append(v + 1)
        chk = 1

    for i in d[v]:
        if o == i: continue
        dfs(v, i, n + 1)

    if chk == 1:
        de[C[v]] = 0
    return

INF = 10 ** 18
N = int(input())
C = list(map(int, input().split()))
d = [[] for i in range(N)]
de = defaultdict(int)
ans = []
chk = [0] * N
cost = [[] * N for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)
    cost[a - 1].append([1, b - 1])
    cost[b - 1].append([1, a - 1])

kyori = dijkstra(0)

de[C[0]] += 1
ans.append(1)
for i in d[0]:
    dfs(0, i, 1)

ans.sort()
for i in ans:
    print(i)
