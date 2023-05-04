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
cost = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cost[a].append([1, b])
    cost[b].append([1, a])
dp1 = dijkstra(0)
for i in dp1:
    if i == INF:
        print('No')
        exit()
print('Yes')
for i in range(1, N):
    tmp = dp1[i] - 1
    for j in cost[i]:
        if dp1[j[1]] == tmp:
            print(j[1] + 1)
            break
