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

N, M = map(int, input().split())
C = [list(input()) for _ in range(N)]
edge = []
S = 0
G = N + 26

for i in range(N):
    for j in range(24):
        if C[i][j] == '1':
            edge.append([i + 1, N + j + 1, 1])

for i in range(N):
    edge.append([S, i + 1, 10])
for i in range(24):
    edge.append([N + i + 1, G, M])

if 24 * M == maxflow(G, S, G, edge):
    print('Yes')
else:
    print('No')
