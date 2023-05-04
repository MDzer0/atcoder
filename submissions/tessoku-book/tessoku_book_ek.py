from heapq import heappop, heappush

INF = 10 ** 18
N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

dist = [INF] * (N + 1)
kakutei = [False] * (N + 1)
q = []
heappush(q, (0, 1))
dist[1] = 0

while q:
    tmp = heappop(q)
    if kakutei[tmp[1]]: continue
    kakutei[tmp[1]] = True

    for i in G[tmp[1]]:
        if dist[i[0]] > dist[tmp[1]] + i[1]:
            dist[i[0]] = dist[tmp[1]] + i[1]
            heappush(q, (dist[i[0]], i[0]))

ans = [N]
tmp = N
while True:
    if tmp == 1: break
    for i in G[tmp]:
        if dist[tmp] - i[1] == dist[i[0]]:
            tmp = i[0]
            ans.append(tmp)
            break
print(*reversed(ans))
