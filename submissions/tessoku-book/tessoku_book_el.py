import sys
sys.setrecursionlimit(10**6)

def dfs(n, v):
    for i in g[n]:
        if i == v: continue
        dfs(i, n)
        dp[n] = max(dp[n], dp[i] + 1)
    return

N, T = map(int, input().split())
g = [[] for _ in range(N + 1)]

for i in range(N - 1):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)

dp = [0] * (N + 1)
dfs(T, T)
print(*dp[1:])
