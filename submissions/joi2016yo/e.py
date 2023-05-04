from heapq import heappop, heappush
from collections import deque

INF = 10 ** 19

def djikistra():
    kakutei = [False] * (N + 1)
    dist = [INF] * (N + 1)
    dist[1] = 0
    q = []
    heappush(q, (0, 1))

    while q:
        tmp = heappop(q)
        if kakutei[tmp[1]]: continue
        kakutei[tmp[1]] = True
        if tmp[0] > dist[tmp[1]]: continue

        for i in G[tmp[1]]:
            if zonbi[i]: continue
            ryokin = P
            if kiken[i]: ryokin = Q
            if i == N:
                dist[i] = min(dist[i], dist[tmp[1]])
            elif dist[i] > dist[tmp[1]] + ryokin:
                dist[i] = dist[tmp[1]] + ryokin
                heappush(q, (dist[i], i))
    return dist

N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
C = [int(input()) for _ in range(K)]
G = [[] for _ in range(N + 1)]
AB = [list(map(int, input().split())) for _ in range(M)]

for i in AB:
    G[i[0]].append(i[1])
    G[i[1]].append(i[0])

kiken = [False] * (N + 1)
zonbi = [False] * (N + 1)
que = deque()
for i in C:
    que.append((i, 0))
    kiken[i] = True
    zonbi[i] = True

while que:
    tmp = que.popleft()
    for i in G[tmp[0]]:
        if kiken[i]: continue
        if tmp[1] + 1 > S: continue
        kiken[i] = True
        que.append((i, tmp[1] + 1))

ansList = djikistra()
print(ansList[-1])
