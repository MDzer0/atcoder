from heapq import heappop, heappush

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

INF = 10 ** 18
N, M = map(int, input().split())
cost = [[] * N for _ in range(N)]
jiko = [INF] * N
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a].append([c, b])
    if a == b:
        jiko[a] = min(jiko[a], c)

dist = []
for i in range(N):
    dist.append(dijkstra(i))

for i in range(N):
    ans = INF
    for j in range(N):
        if i == j:
            ans = min(jiko[i], ans)
        else:
            ans = min(ans, dist[i][j] + dist[j][i])
    if ans == INF:
        print(-1)
    else:
        print(ans)
