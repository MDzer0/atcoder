from heapq import heappop, heappush

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

INF = 10 ** 18
n, x, y = map(int, input().split())
cost = [[] for _ in range(n)]

for i in range(n - 1):
    a = i
    b = i + 1
    cost[a].append([1, b])
    cost[b].append([1, a])
cost[x - 1].append([1, y - 1])
cost[y - 1].append([1, x - 1])
ans = [0] * n
for i in range(n - 1):
    dp1 = dijkstra(i)
    for j in dp1[i:]:
        ans[j] += 1

for i in ans[1:]:
    print(i)
