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
N = int(input())
cost = [[] for _ in range(N)]
for i in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cost[a].append([c, b])
    cost[b].append([c, a])

Q, K = map(int, input().split())
dp1 = dijkstra(K - 1)
for i in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ans = dp1[x] + dp1[y]
    print(ans)
