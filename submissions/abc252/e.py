from heapq import heappop, heappush

INF = 10 ** 19
def dijkstra():
    kakutei = [False] * (N + 1)
    dist = [INF] * (N + 1)
    dist[1] = 0
    q = []
    heappush(q, (0, 1))
    ans = [-1] * (N + 1)

    while q:
        tmp = heappop(q)
        if kakutei[tmp[1]]: continue
        kakutei[tmp[1]] = True
        for i in G[tmp[1]]:
            if dist[i[0]] > dist[tmp[1]] + i[1]:
                dist[i[0]] = dist[tmp[1]] + i[1]
                ans[i[0]] = i[2]
                heappush(q, (dist[i[0]], i[0]))
    return ans

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c, i + 1))
    G[b].append((a, c, i + 1))

ans = dijkstra()
print(*ans[2:])
