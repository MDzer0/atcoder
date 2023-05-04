from heapq import heappop, heappush

INF = 10 ** 19

def djikstra(start):
    dist = [INF] * (n + 1)
    kakutei = [False] * (n + 1)
    q = []
    dist[start] = 0
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
n, k = map(int, input().split())
G = [[] for _ in range(n + 1)]

for i in range(k):
    inputList = list(map(int, input().split()))
    if inputList[0] == 1:
        G[inputList[1]].append((inputList[2], inputList[3]))
        G[inputList[2]].append((inputList[1], inputList[3]))
    else:
        ans = djikstra(inputList[1])
        if ans[inputList[2]] != INF:
            print(ans[inputList[2]])
        else:
            print(-1)
