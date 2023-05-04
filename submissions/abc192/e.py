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
                if dp[v] % i[2] != 0:
                    if dp[v] < i[2]:
                        i[0] += i[2] - dp[v]
                    else:
                        i[0] += i[2] - (dp[v] % i[2])
                heappush(hq, [i[0] + dp[v], i[1]])
    return dp

INF = 10 ** 18
N, M, X, Y = map(int, input().split())
abtk = [list(map(int, input().split())) for _ in range(M)]
cost = [[] for _ in range(N)]

for i in abtk:
    cost[i[0] - 1].append([i[2], i[1] - 1, i[3]])
    cost[i[1] - 1].append([i[2], i[0] - 1, i[3]])

ans = dijkstra(X - 1)
if ans[Y - 1] == INF:
    print(-1)
else:
    print(ans[Y - 1])
