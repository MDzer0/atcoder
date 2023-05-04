from heapq import heappop, heappush
INF = 10 ** 18

def dijkstra(s):
    used = [1] * n
    dp = [INF] * n
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

n, u, v = map(int, input().split())
cost = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cost[a].append([1, b])
    cost[b].append([1, a])

dp1 = dijkstra(v - 1)
dp2 = dijkstra(u - 1)
ans = 0
for i in range(n):
    if dp1[i] >= dp2[i]:
        ans = max(ans, dp1[i])

print(ans - 1)
