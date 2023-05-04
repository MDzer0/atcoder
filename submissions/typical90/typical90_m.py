from heapq import heappop, heappush
INF = 10 ** 19

def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    kakutei = [False] * (N + 1)
    q = []
    heappush(q, (0, start))

    while q:
        tmp = heappop(q)
        if kakutei[tmp[1]]: continue
        kakutei[tmp[1]] = True
        for i in G[tmp[1]]:
            if dist[i[0]] > dist[tmp[1]] + i[1]:
                dist[i[0]] = dist[tmp[1]] + i[1]
                heappush(q, (dist[i[0]], i[0]))
    return dist

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

leftList = dijkstra(1)
rightList = dijkstra(N)

for i in range(1, N + 1):
    print(leftList[i] + rightList[i])
