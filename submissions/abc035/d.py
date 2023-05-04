from heapq import heappop, heappush

def dijkstra(s, cost):
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
N, M, T = map(int, input().split())
alst = list(map(int, input().split()))
ikilst = [[] for _ in range(N)]
kaerilst = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    ikilst[a].append([c, b])
    kaerilst[b].append([c, a])

d1 = dijkstra(0, ikilst)
d2 = dijkstra(0, kaerilst)

ans = alst[0] * T
for i in range(1, N):
    tmp = T - d1[i] - d2[i]
    if tmp < 0:
        continue
    ans = max(ans, alst[i] * tmp)

print(ans)
