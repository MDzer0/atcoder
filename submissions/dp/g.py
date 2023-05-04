import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    if dp[v] != 0: return dp[v]
    cnt = 0
    for i in g[v]:
        cnt = max(cnt, dfs(i) + 1)
    dp[v] = cnt
    return dp[v]

N, M = map(int, input().split())
dp = [0] * (N + 1)
g = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)

for i in range(N):
    dfs(i)

print(max(dp))
