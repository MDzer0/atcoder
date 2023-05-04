from heapq import heappop, heappush
INF = 10 ** 19

def dijkstra(G):
    dist = [INF] * (N + 1)
    dist[1] = 0
    kakutei = [False] * (N + 1)

    q = []
    heappush(q, (0, 1))
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
ABCD = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N + 1)]

for i in ABCD:
    if i[3] == 1:
        G[i[0]].append((i[1], 10000 * i[2] - 1))
        G[i[1]].append((i[0], 10000 * i[2] - 1))
    else:
        G[i[0]].append((i[1], 10000 * i[2]))
        G[i[1]].append((i[0], 10000 * i[2]))

ansList = dijkstra(G)
kyori  = (ansList[N] + 9999) // 10000
ki = kyori * 10000 - ansList[N]
print(kyori, ki)
