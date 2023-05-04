INF = 10 ** 18
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

def dfs(pos, goal, F, G, used):
    if pos == goal:
        return F
    used[pos] = True
    for e in G[pos]:
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), G, used)
            if flow >= 1:
                e.cap -= flow
                G[e.to][e.rev].cap += flow
                return flow
    return 0

def maxflow(N, s, t, edges):
    G = [[] for _ in range(N + 1)]
    for a, b, c in edges:
        G[a].append(maxflow_edge(b, c, len(G[b])))
        G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))

    total_flow = 0
    while True:
        used = [False] * (N + 1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break
    return total_flow

N = int(input())
a = list(map(int, input().split()))
S = 0
G = N + 1
edge = []
ans = 0

for i in range(N):
    if a[i] >= 0:
        ans += a[i]
        edge.append([S, i + 1, a[i]])
    else:
        edge.append([i + 1, G, -a[i]])

for i in range(1, N + 1):
    for j in range(2, N + 1):
        if i * j <= N:
            edge.append([i * j, i, INF])

print(ans - maxflow(G, S, G, edge))
