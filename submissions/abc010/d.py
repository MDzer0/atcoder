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
    INF = 10 ** 10
    total_flow = 0
    while True:
        used = [False] * (N + 1)
        F = dfs(s, t, INF, G, used)
        if F > 0:
            total_flow += F
        else:
            break
    return total_flow

N, G, E = map(int, input().split())
p = list(map(int, input().split()))
edges = []
for i in range(E):
    a, b = map(int, input().split())
    edges.append([a, b, 1])
    edges.append([b, a, 1])

for i in p:
    edges.append([i, N, 1])
    edges.append([N, i, 1])
ans = maxflow(N, 0, N, edges)
print(ans)
