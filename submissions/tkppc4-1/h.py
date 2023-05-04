from heapq import heappop, heappush
INF = 10 ** 19

def dijkstra():
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
            jikan = dist[tmp[1]]
            if tmp[1] != 1 and tmp[1] != N:
                jikan += t[tmp[1] - 2]
                jikan += (i[2] - (jikan % i[2]))

            jikan += i[1]
            if dist[i[0]] > jikan:
                dist[i[0]] = jikan
                heappush(q, (dist[i[0]], i[0]))
    return dist

N, M, K = map(int, input().split())
t = [int(input()) for _ in range(N - 2)]
abcd = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N + 1)]

for i in abcd:
    G[i[0]].append((i[1], i[2], i[3]))
    G[i[1]].append((i[0], i[2], i[3]))

ansDist = dijkstra()
if ansDist[N] <= K:
    print(ansDist[N])
else:
    print(-1)
